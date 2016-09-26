//
// Created by alihitawala on 9/11/16.
// modified by kshiteejm
//

#ifndef UDPECHO_MASTER_PACKET_H
#define UDPECHO_MASTER_PACKET_H

struct Packet {
    int seq_num;
    int length;
    char* data;
    
    /*
    Packet(int length = 1460)
        : seq_num(0), length(length),
          data(new char[length])
    {
    }
    */

    Packet(int length = 1460, int seq_num = 0)
        : seq_num(seq_num), length(length),
          data(new char[length])
    {
    }

    ~Packet()
    {
        delete [] data;
    }
};

// alternate creation style for Packet
Packet* createPacket(int length) {
    Packet *pkt = (Packet *) malloc(length);
    pkt->seq_num = 0;
    pkt->length = length;
    return pkt;
}

// alternate creation style for Packet
Packet* createPacket(int length, int seq_num) {
    Packet* pkt = (Packet *) malloc(length);
    pkt->seq_num = seq_num;
    pkt->length = length;
    return pkt;
}

char* serialize(Packet* pkt) {
    char* data = (char *) malloc(pkt->length);
    int* h = (int*)data;
    *h = pkt->seq_num; h++;
    *h = pkt->length; h++;

    char* d = (char*)h;
    int i = 0;
    int max = pkt->length - 2*sizeof(int);
    while (i < max) {
        *d = pkt->data[i];
        d++; i++;
    }
    return data;
}

Packet* deserialize(char* data) {
    int* h = (int*)data;
    int seq_num = *h; h++;
    int length = *h; h++;
    
    Packet pkt(length, seq_num);

    char* d = (char*)h;
    int i = 0;
    int max = pkt.length - 2*sizeof(int);
    while (i < max) {
        pkt.data[i] = *d;
        d++; i++;
    }
    return &pkt;
}

/*
void deserialize(char* data, Packet* pkt) {
    int* h = (int*)data;
    pkt->seq_num = *h; h++;
    pkt->length = *h; h++;

    char* d = (char*)h;
    int i = 0;
    int max = pkt->length - 2*sizeof(int);
    while (i < max) {
        pkt->data[i] = *d;
        d++; i++;
    }
}
*/

#endif //UDPECHO_MASTER_PACKET_H
