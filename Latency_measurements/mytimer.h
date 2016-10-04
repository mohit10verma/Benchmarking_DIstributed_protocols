unsigned long long int GetRDTSC() {
  volatile int dont_remove __attribute__((unused)); // volatile to stop optimizing                                                                                                 
  unsigned hi, lo, a, b;

  __asm ( "mov %1, %%eax; "            // a into eax                                                                                                                               
          "cpuid;"
          "mov %%eax, %0;"             // eax into b                                                                                                                               
          :"=r"(b)                     // output                                                                                                                                   
          :"r"(a)                      // input                                                                                                                                    
          :"%eax","%ebx","%ecx","%edx" // clobbered register                                                                                                                       
          );

  __asm__ __volatile__("rdtsc":          // read of tsc                                                                                                                            
		       "=a"(lo), "=d"(hi));
  return ( (unsigned long long)lo)|( ((unsigned long long)hi)<<32 );
}

//Function to set processor no.                                                                                                                                                    
void SetAffinity(unsigned long corenum)
{
  cpu_set_t my_set;        /* Define your cpu_set bit mask. */
  CPU_ZERO(&my_set);       /* Initialize it all to 0, i.e. no CPUs selected. */
  CPU_SET(corenum, &my_set);     /* set the bit that represents core 0. */
  sched_setaffinity(0, sizeof(cpu_set_t), &my_set);
}


