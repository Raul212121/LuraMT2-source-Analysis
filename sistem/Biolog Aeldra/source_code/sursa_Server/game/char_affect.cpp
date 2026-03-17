# AFTER

	while (it != m_list_pkAffect.end())
	{
		CAffect * pkAff = *it;

		if (bSave)
		{
			if ( IS_NO_CLEAR_ON_DEATH_AFFECT(pkAff->dwType) || IS_NO_SAVE_AFFECT(pkAff->dwType) )
			{
				++it;
				continue;
			}

# ADD

#ifdef __ENABLE_BIOLOG_SYSTEM__
			if (pkAff->dwType >= AFF_BIO_1 && pkAff->dwType <= AFF_BIO_20)
			{
				++it;
				continue;
			}
#endif