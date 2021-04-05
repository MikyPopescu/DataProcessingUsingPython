CREATE TABLE t_clienti_leasing as select * from ms_dba.t_clienti_leasing;

CREATE TABLE t_clienti_daune as select * from ms_dba.t_clienti_daune;

CREATE TABLE clienti_noi as select * from t_clienti_leasing where 2=3;


insert into clienti_noi  select * from t_clienti_leasing;
commit;
--select * from clienti_noi;
select * from clienti_noi where nume_client like 'Popa Marcel%';

