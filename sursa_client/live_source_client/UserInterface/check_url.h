#include "StdAfx.h"
#if defined(CHECK_WEB_URL)

#include <curl/curl.h>

#pragma comment (lib, "crypt32.lib")
#pragma comment (lib, "advapi32")
#pragma comment (lib, "ws2_32.lib")
#pragma comment (lib, "wldap32.lib")
#pragma comment (lib, "normaliz.lib")


static size_t URL_WriteResponseCallback(void* contents, size_t size, size_t nmemb, void* userp)
{

	((std::string*)userp)->append((char*)contents, size * nmemb);
	return size * nmemb;
}

bool URL_CheckWebResponse()
{
	CURL* _c;
	if (!(_c = curl_easy_init()))
		return false;
	
	std::string _rBffr;
	curl_easy_setopt(_c, CURLOPT_URL, METIN2_SERVER_IP);
	curl_easy_setopt(_c, CURLOPT_WRITEFUNCTION, URL_WriteResponseCallback);
	curl_easy_setopt(_c, CURLOPT_WRITEDATA, &_rBffr);
	
	CURLcode _r = curl_easy_perform(_c);
	curl_easy_cleanup(_c);

	return (_r == CURLE_OK);
}
#endif
