/*
 *
 * Copyright 2015, Google Inc.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are
 * met:
 *
 *     * Redistributions of source code must retain the above copyright
 * notice, this list of conditions and the following disclaimer.
 *     * Redistributions in binary form must reproduce the above
 * copyright notice, this list of conditions and the following disclaimer
 * in the documentation and/or other materials provided with the
 * distribution.
 *     * Neither the name of Google Inc. nor the names of its
 * contributors may be used to endorse or promote products derived from
 * this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 * A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 * OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 * LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 * DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 * THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 */

#include <iostream>
#include <memory>
#include <string>
#include <sys/types.h>
#include <grpc++/grpc++.h>
#include <stdint.h>
#include <sys/time.h>
#include "helloworld.grpc.pb.h"
#include "mytimer.h"
#define BILLION 1000000000L
using grpc::Channel;
using grpc::ClientContext;
using grpc::Status;
using helloworld::HelloRequest;
using helloworld::HelloReply;
using helloworld::Greeter;
using helloworld::HelloInteger;
using helloworld::HelloDouble;
using helloworld::Person;
using helloworld::Person_PhoneNumber;
using helloworld::Person_PhoneType;


class GreeterClient {
	public:
		GreeterClient(std::shared_ptr<Channel> channel)
			: stub_(Greeter::NewStub(channel)) {}

		// Assambles the client's payload, sends it and presents the response back
		// from the server.

		std::string SayHello(const std::string& user) {
			// Data we are sending to the server.
			HelloRequest request;
			request.set_name(user);



			// Container for the data we expect from the server.
			HelloReply reply;

			// Context for the client. It could be used to convey extra information to
			// the server and/or tweak certain RPC behaviors.
			ClientContext context;

			// The actual RPC.
			Status status = stub_->SayHello(&context, request, &reply);

			// Act upon its status.
			if (status.ok()) {
				return reply.message();
			} else {
				std::cout << status.error_code() << ": " << status.error_message()
					<< std::endl;
				return "RPC failed";
			}
		}

	private:
		std::unique_ptr<Greeter::Stub> stub_;
};

void printcpuinfo (void) {
	FILE *cpuinfo = fopen("/proc/cpuinfo", "rb");
	char *arg = 0;
	size_t size = 0;
	while(getdelim(&arg, &size, 0, cpuinfo) != -1)
	{
		puts(arg);
	}
	free(arg);
	fclose(cpuinfo);
}


uint64_t gettimetomarshall(const::std::string& str) { //Returns number of cycles
  uint64_t start, end, t;
	HelloRequest req;
	req.set_name(str);
	void* data = (void*) new char[str.length()];

	start = GetRDTSC();
	req.SerializeToArray(data, str.length());
	end = GetRDTSC();
	delete [] (char*) data;
	t = end - start;
	std::cout<<t << std::endl;
	return t;
}


uint64_t gettimetomarshall(double i) { //Returns number of cycles
  uint64_t start, end, t;
	HelloDouble req;
	req.set_value(i);
	void* data = (void*) new char[sizeof(double)];
	start = GetRDTSC();
	req.SerializeToArray(data, sizeof(double));

	end = GetRDTSC();

	delete [] (char*) data;
	t = end - start;

	std::cout<<t << std::endl;
	return t;
}

uint64_t gettimetomarshall(int i) { //Returns number of cycles

	uint64_t start, end, t;
	HelloDouble req;
	req.set_value(i);
	void* data = (void*) new char[sizeof(int)];

	start = GetRDTSC();
	req.SerializeToArray(data, sizeof(int));
	end = GetRDTSC();
	delete [] (char*) data;
	
	t = end-start;
	std::cout<<t << std::endl;
	return t;
}

uint64_t gettimetomarshallstruct(void) {
	uint64_t start, end, t;
	Person p;
	p.set_name("Mohit Verma");
	p.set_id(12356988);
	p.set_email("mohit93@cs.wisc.edu");
	Person_PhoneNumber *a;
	a = p.add_phone();
	a->set_type((Person_PhoneType)1);
	a->set_number("682345657687543");

	void* data = (void*) new char[p.ByteSize()];

	start = GetRDTSC();
	p.SerializeToArray(data, sizeof(int));
	end = GetRDTSC();
	delete [] (char*) data;
	
	t = end-start;
	std::cout<<t << std::endl;
	return t;

}

int main(int argc, char** argv) {
	// Instantiate the client. It requires a channel, out of which the actual RPCs
	// are created. This channel models a connection to an endpoint (in this case,
	// localhost at port 50051). We indicate that the channel isn't authenticated
	// (use of InsecureChannelCredentials()).
	//printcpuinfo();

	SetAffinity(0);
	GreeterClient greeter(grpc::CreateChannel(
				"localhost:50051", grpc::InsecureChannelCredentials()));
	std::string user("world");
	uint64_t begin, end, time = 0;

	
	//time = gettimetomarshall("fasasddsfssdxcgvjhjkbkjhiouiytrszdxffjghjkl,vccseertyryuuiijoiuyytrefssddsfsfasasddsfssddsfsfasasddsfssdds1234348680kjhg2143567");
	begin = GetRDTSC();
	std::string reply = greeter.SayHello(user);
        end = GetRDTSC();
	std::cout << begin << std::endl;
	std::cout <<end << std::endl;
	/*	time = gettimetomarshall("fqwertyuasdfghjkafqwertyuafgfghjkafqwlktyuasdfghjka12wertyuasdfgfqwertyuasdfghjkafqwertyuafgfghjkafqwlktyuasdfghjka12wertyuasdf1fqwertyuasdfghjkafqwertyuafgfghjkafqwlktyuasdfghjka12wertyuasdfgfqwertyuasdfghjkafqwertyuafgfghjkafqwlktyuasdfghjkaklwertyu67df1fqwertyuasdfghjkafqwertyuafgfghjkafqwlktyuasdfghjka12wertyuasdfgfqwertyuasdfghjkafqwertyuafgfghjkafqwlktyuasdfghjka12wertyuasdf1fqwertyuasdfghjkafqwertyuafgfghjkafqwlktyuasdfghjka12wertyuasdfgfqwertyuasdfghjkafqwertyuafgfghjkafqwlktyuasdfghjkaklwertyu67df1fqwertyuasdfghjkafqwertyuafgfghjkafqwlktyuasdfghjka12wertyuasdfgfqwertyuasdfghjkafqwertyuafgfghjkafqwlktyuasdfghjka12wertyuasdf1fqwertyuasdfghjkafqwertyuafgfghjkafqwlktyuasdfghjka12wertyuasdfgfqwertyuasdfghjkafqwertyuafgfghjkafqwlktyuasdfghjkaklwertyu67df1fqwertyuasdfghjkafqwertyuafgfghjkafqwlktyuasdfghjka12wertyuasdfgfqwertyuasdfghjkafqwertyuafgfghjkafqwlktyuasdfghjka12wertyuasdf1fqwertyuasdfghjkafqwertyuafgfghjkafqwlktyuasdfghjka12wertyuasdfgfqwertyuasdfghjkafqwertyuafgfghjkafqwlktyuasdfghjkaklwertyu67df1fqwertyuasdfghjkafqwertyuafgfghjkafqwlktyuasdfghjka12wertyuasdfgfqwertyuasdfghjkafqwertyuafgfghjkafqwlktyuasdfghjka12wertyuasdf1fqwertyuasdfghjkafqwertyuafgfghjkafqwlktyuasdfghjka12wertyuasdfgfqwertyuasdfghjkafqwertyuafgfghjkafqwlktyuasdfghjkaklwertyu67df1fqwertyuasdfghjkafqwertyuafgfghjkafqwlktyuasdfghjka12wertyuasdfgfqwertyuasdfghjkafqwertyuafgfghjkafqwlktyuasdfghjka12wertyuasdf1fqwertyuasdfghjkafqwertyuafgfghjkafqwlktyuasdfghjka12wertyuasdfgfqwertyuasdfghjkafqwertyuafgfghjkafqwlktyuasdfghjkaklwertyu67df1fqwertyuasdfghjkafqwertyuafgfghjkafqwlktyuasdfghjka12wertyuasdfgfqwertyuasdfghjkafqwertyuafgfghjkafqwlktyuasdfghjka12wertyuasdf1fqwertyuasdfghjkafqwertyuafgfghjkafqwlktyuasdfghjka12wertyuasdfgfqwertyuasdfghjkafqwertyuafgfghjkafqwlktyuasdfghjkaklwertyu67df1fqwertyuasdfghjkafqwertyuafgfghjkafqwlktyuasdfghjka12wertyuasdfgfqwertyuasdfghjkafqwertyuafgfghjkafqwlktyuasdfghjka12wertyuasdf1fqwertyuasdfghjkafqwertyuafgfghjkafqwlktyuasdfghjka12wertyuasdfgfqwertyuasdfghjkafqwertyuafgfghjkafqwlktyuasdfghjkaklwertyu67df1");*/
	//time = gettimetomarshall(3898990713.00);
	//time = gettimetomarshall(3898);
	//	time = gettimet
	//time = gettimetomarshallstruct();
	//std::cout << "Greeter received: " << reply << std::endl;

	return 0;
}
