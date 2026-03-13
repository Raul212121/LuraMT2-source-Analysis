#pragma once

#include "../eterLib/StdAfx.h"
#include "../eterGrnLib/StdAfx.h"

#include "../UserInterface/Locale_inc.h"

#ifdef BYTE
#undef BYTE
#endif

#ifdef AT
#undef AT
#endif

#pragma warning(push)
#pragma warning(disable:5033) // warning C5033: 'register' is no longer a supported storage class
#include <python2/python.h>
#include <python2/node.h>
#include <python2/grammar.h>
#include <python2/token.h>
#include <python2/parsetok.h>
#include <python2/errcode.h>
#include <python2/compile.h>
#include <python2/eval.h>
#include <python2/marshal.h>
#pragma warning(pop)

#ifdef BYTE
#undef BYTE
#endif

#ifdef AT
#undef AT
#endif
#include "PythonUtils.h"
#include "PythonLauncher.h"
#include "Resource.h"

void initdbg();
