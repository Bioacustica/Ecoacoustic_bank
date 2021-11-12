INSERT INTO bioacustica.label (id_label, id_type, description)
VALUES (3, 3,'rana platanera');


INSERT INTO bioacustica.type (id_type,description)
VALUES (3,'ranas');

SELECT label.id_label, label.id_type, label.description, type.description
FROM label
INNER JOIN type ON type.id_type=label.id_type;



ALTER TABLE label ENABLE ROW LEVEL SECURITY;
ALTER POLICY labels2 ON label TO daniel1
USING (id_type in (SELECT id_type FROM seguridad WHERE usuario = 'daniel'))



SELECT label.id_label, label.id_type, label.description, type.description
FROM label
INNER JOIN type ON type.id_type=label.id_type;

ALTER ROLE animalesitm SET search_path TO bioacustica;
ALTER DATABASE animalesitm SET search_path TO bioacustica;
SHOW search_path;

SELECT * FROM seguridad;


CREATE TABLE seguridad (
    id_segur int,
    usuario varchar(255),
    id_type int
);

INSERT INTO seguridad (id_segur,usuario, id_type)
VALUES (1,'daniel', 3);
GRANT SELECT ON TABLE seguridad TO daniel1
-------------------------------------------------------------------
create or replace function bioacustica.create_user_usuario (
  unm varchar,
  pwd varchar
)
  returns varchar(10) as $$

begin

  execute format($f$create role %I login password '%s'$f$,unm,pwd);
  execute format('alter role %I NOSUPERUSER NOCREATEDB NOCREATEROLE',unm);
  execute format('alter role %I SET search_path TO bioacustica',unm);
  execute format('REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA bioacustica FROM %I',unm);
  execute format('REVOKE USAGE ON SCHEMA bioacustica FROM %I',unm);
  execute format('GRANT USAGE ON SCHEMA bioacustica TO %I',unm);
  execute format('SET search_path TO bioacustica');
  execute format('GRANT SELECT ON TABLE label, type, labeled TO %I ',unm);
  execute format('GRANT SELECT ON TABLE record, record_obs, record_path, format, season, project, habitat TO %I ',unm);
  return 'success';



end;
$$ language plpgsql;

SELECT create_user_usuario('daniel1', '123456789');
--------------------------------------------------------------------------------------------------------------------
create or replace function bioacustica.filter(
  	etiqueta varchar,
  	tipo_etiqueta varchar
	
)
  returns varchar(10) as $$

begin

  execute format($f$create role %I login password '%s'$f$,unm,pwd);
  execute format('alter role %I NOSUPERUSER NOCREATEDB NOCREATEROLE',unm);
  execute format('alter role %I SET search_path TO bioacustica',unm);
  execute format('REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA bioacustica FROM %I',unm);
  execute format('REVOKE USAGE ON SCHEMA bioacustica FROM %I',unm);
  execute format('GRANT USAGE ON SCHEMA bioacustica TO %I',unm);
  execute format('SET search_path TO bioacustica');
  execute format('GRANT SELECT ON TABLE label, type, labeled TO %I ',unm);
  execute format('GRANT SELECT ON TABLE record, record_obs, record_path, format, season, project, habitat TO %I ',unm);
  return 'success';



end;
$$ language plpgsql;
------------------------------

insert into seguridad(id_segur,usuario, id_type)
VALUES (4,'daniel2',select id_label from label where id_type=2);

INSERT INTO seguridad
    SELECT id, time 
    FROM dblink('dbname=dbtest', 'SELECT id, time FROM tblB')
    AS t(id integer, time integer)
    WHERE time > 1000;
	
-----------------------------------------------
DEF function filter(parameter_1, parameter_2, ...parameter_n, username)-- con n finito
 	SELECT record_id
	FROM X_tabla
	INNER JOIN Y_tabla ON Y_tabla.parameter_1=X_table.parameter_1
	INNER JOIN Z_tabla ON Z_tabla.parameter_2=(X_table o Y_table).parameter_2
	WHERE parameter_1 = x_cosa y WHERE parameter_2 = y_cosa...
	el resultado de el anterior SELECT sería una lista de ids que debo insertar en otra tabla :(  
		
	insert into seguridad(id_segur,usuario, record_id)
	-- usuario es username y es igual para todos los record_id que coincidan del filtro
	-- el id_segur seria el id unico para cada registro pero no es como que lo necesite así que podria ser una tabla huerfanita
		
---------------------------------------------------------------------------------------------------
SELECT label.id_label, label.id_type, label.description, type.description
FROM label
INNER JOIN type ON type.id_type=label.id_type;
		
create or replace function bioacustica.get_join(etiqueta varchar) 
	returns table (
		label varchar,
		type varchar
	) 
	language plpgsql
as $$
begin
	return query 
		select
			label.description,
			type.description
		from
			label
		INNER JOIN type ON type.id_type=label.id_type;
		where
			label.description = etiqueta;
end;$$