# ADD AT THE TOP # IF YOU DOESNT HAVE Extern/include/boost/date_time download this from
- https://www.boost.org/
# THEN REPLACE THE WHOLE BOOST

#include <boost/date_time/posix_time/posix_time.hpp>
#include <boost/date_time/c_local_time_adjustor.hpp>

# ADD AT THE BOTTOM OF FILE

std::string GetFullDateFromTime(time_t&& end_time_sec, bool bWhiteSpace)
{
	using boost::posix_time::ptime;
	using namespace boost::posix_time;
	using adj = boost::date_time::c_local_adjustor<ptime>;
	auto endTime = adj::utc_to_local(from_time_t(end_time_sec));

	char t_buf[256];
	if (bWhiteSpace)
		snprintf(t_buf, sizeof(t_buf), "%d-%s%d-%s%d %s%d:%s%d:%s%d", static_cast<int>(endTime.date().year()),
			static_cast<int>(endTime.date().month().as_number()) <= 9 ? "0" : "", static_cast<int>(endTime.date().month().as_number()),
			static_cast<int>(endTime.date().day().as_number()) <= 9 ? "0" : "", static_cast<int>(endTime.date().day().as_number()),
			static_cast<int>(endTime.time_of_day().hours()) <= 9 ? "0" : "", static_cast<int>(endTime.time_of_day().hours()),
			static_cast<int>(endTime.time_of_day().minutes()) <= 9 ? "0" : "", static_cast<int>(endTime.time_of_day().minutes()),
			static_cast<int>(endTime.time_of_day().seconds()) <= 9 ? "0" : "", static_cast<int>(endTime.time_of_day().seconds()));
	else
		snprintf(t_buf, sizeof(t_buf), "%d-%s%d-%s%d_%s%d:%s%d:%s%d", static_cast<int>(endTime.date().year()),
			static_cast<int>(endTime.date().month().as_number()) <= 9 ? "0" : "", static_cast<int>(endTime.date().month().as_number()),
			static_cast<int>(endTime.date().day().as_number()) <= 9 ? "0" : "", static_cast<int>(endTime.date().day().as_number()),
			static_cast<int>(endTime.time_of_day().hours()) <= 9 ? "0" : "", static_cast<int>(endTime.time_of_day().hours()),
			static_cast<int>(endTime.time_of_day().minutes()) <= 9 ? "0" : "", static_cast<int>(endTime.time_of_day().minutes()),
			static_cast<int>(endTime.time_of_day().seconds()) <= 9 ? "0" : "", static_cast<int>(endTime.time_of_day().seconds()));

	return t_buf;
}

std::string GetFullDateFromTime(const time_t& end_time_sec, bool bWhiteSpace)
{
	using boost::posix_time::ptime;
	using namespace boost::posix_time;
	using adj = boost::date_time::c_local_adjustor<ptime>;
	auto endTime = adj::utc_to_local(from_time_t(end_time_sec));

	char t_buf[256];
	if (bWhiteSpace)
		snprintf(t_buf, sizeof(t_buf), "%d-%s%d-%s%d %s%d:%s%d:%s%d", static_cast<int>(endTime.date().year()),
			static_cast<int>(endTime.date().month().as_number()) <= 9 ? "0" : "", static_cast<int>(endTime.date().month().as_number()),
			static_cast<int>(endTime.date().day().as_number()) <= 9 ? "0" : "", static_cast<int>(endTime.date().day().as_number()),
			static_cast<int>(endTime.time_of_day().hours()) <= 9 ? "0" : "", static_cast<int>(endTime.time_of_day().hours()),
			static_cast<int>(endTime.time_of_day().minutes()) <= 9 ? "0" : "", static_cast<int>(endTime.time_of_day().minutes()),
			static_cast<int>(endTime.time_of_day().seconds()) <= 9 ? "0" : "", static_cast<int>(endTime.time_of_day().seconds()));
	else
		snprintf(t_buf, sizeof(t_buf), "%d-%s%d-%s%d_%s%d:%s%d:%s%d", static_cast<int>(endTime.date().year()),
			static_cast<int>(endTime.date().month().as_number()) <= 9 ? "0" : "", static_cast<int>(endTime.date().month().as_number()),
			static_cast<int>(endTime.date().day().as_number()) <= 9 ? "0" : "", static_cast<int>(endTime.date().day().as_number()),
			static_cast<int>(endTime.time_of_day().hours()) <= 9 ? "0" : "", static_cast<int>(endTime.time_of_day().hours()),
			static_cast<int>(endTime.time_of_day().minutes()) <= 9 ? "0" : "", static_cast<int>(endTime.time_of_day().minutes()),
			static_cast<int>(endTime.time_of_day().seconds()) <= 9 ? "0" : "", static_cast<int>(endTime.time_of_day().seconds()));

	return t_buf;
}

