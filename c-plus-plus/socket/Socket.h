#ifndef _SOCKET_H_
#define _SOCKET_H_
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <unistd.h>
#include <string>
#include <arpa/inet.h>

const int MAXHOSTNAME = 200;
const int MAXCONNECTIONS = 5;
const int MAXRECV = 500; 

class Socket {
	private:
		int m_sock;
		sockaddr_in m_addr;
	public:
		Socket();
		virtual ~Socket();
		//server initialization
		bool create();
		bool bind (const int port);
		bool listen() const;
		bool accept (Socket &) const;

		//client initialization
		bool connect (const std::string host,const int port);

		//Data transimission
		bool send (const std::string) const;
		int recv (std::string &) const;

		void set_non_blocking ( const bool );
		bool is_valid() const
		{
			return m_sock != -1;
		}
};


#endif
