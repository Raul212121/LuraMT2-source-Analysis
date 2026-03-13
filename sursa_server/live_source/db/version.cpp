#include "stdafx.h"
#include <mariadb/mariadb_version.h>

void WriteVersion()
{
	FILE* fp(fopen("VERSION.txt", "w"));

	if (fp)
	{
		fprintf(fp, "__TIMESTAMP__: %s\n", __TIMESTAMP__);
		fprintf(fp, "__ARCHITECTURE__: %s\n", __ARCHITECTURE__);
		fprintf(fp, "__TOOLSET__: %s\n", __TOOLSET__);
		fprintf(fp, "__BUILD_TYPE__: %s\n", __BUILD_TYPE__);
		fprintf(fp, "__HOSTNAME__: %s\n", __HOSTNAME__);
		fprintf(fp, "__TARGET_OS__: %s\n", __TARGET_OS__);
		fprintf(fp, "__PREMAKE_VERSION__: %s\n", __PREMAKE_VERSION__);
		fprintf(fp, "__WORKING_DIR__: %s\n", __WORKING_DIR__);
		fprintf(fp, "__GIT_REVISION_HASH__: %s\n", __GIT_REVISION_HASH__);
		fprintf(fp, "__MARIADB_CLIENT_VERSION__: %s\n", MARIADB_CLIENT_VERSION_STR);
		fprintf(fp, "__MARIADB_BASE_VERSION__: %s\n", MARIADB_BASE_VERSION);
		fprintf(fp, "__MYSQL_SERVER_VERSION__: %s\n", MYSQL_SERVER_VERSION);
		fclose(fp);
	}
	else
	{
		fprintf(stderr, "cannot open VERSION.txt\n");
		exit(0);
	}
}

