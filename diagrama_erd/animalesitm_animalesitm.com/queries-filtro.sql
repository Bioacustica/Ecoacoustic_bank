create or replace function bioacustica.get_join(
	catalogo varchar default NULL,
	habitat_q varchar default NULL,
	municipio varchar default NULL,
	evento_q varchar default NULL,
	tipo_case varchar default NULL,
	tipo_micro varchar default NULL,
	metodo_etiquetado varchar default NULL,
	software_q varchar default NULL,
	tipo_grabadora varchar default NULL
) 
-- Estructura de lo que va a retornar (no se puede cambiar parametros de entrada/salida)
	returns table (
		id_record integer,
		formato_ varchar,
		chunk_ smallint,		-- Número del record asociado al catálogo
		date_ timestamp,
		catalogo_ varchar,
		elevation integer,
		chunks_ smallint,
		tipo_grabadora_ varchar,
		case_ varchar,
		microphone varchar,
		sampling_description varchar,
		habitat_ varchar,
		ciudad_ varchar,
		departamento_ varchar,
		type_ varchar,
		metodo_etiquetado_ varchar,
		software_etiquetado_ varchar
	) 
	
	language plpgsql
as $$
begin
	return query 
		select
			record.id_record,
			format.description,
			record.chunk,
			record.date,
			catalogue.description,
			catalogue.elevation,
			catalogue.chunks,
			hardware.description,
			"case".description,
			microphone.description,
			sampling.description,
			habitat.description,
			municipality.description,
			department.description,
			type.description,
			evidence.description,
			software.descripton
			
		from
			catalogue
		INNER JOIN record ON catalogue.id_catalogue=record.id_catalogue
		--where catalogue.description = (CASE WHEN catalogo IS NOT NULL THEN catalogo ELSE catalogue.description END)
		INNER JOIN format ON record.id_format=format.id_format
		INNER JOIN h_serial ON catalogue.id_h_serial=h_serial.id_h_serial
		INNER JOIN hardware ON h_serial.id_hardware=hardware.id_hardware
		-- " " para que no tome como palabra reservada
		INNER JOIN "case" ON catalogue.id_case="case".id_case
		INNER JOIN microphone ON catalogue.id_microphone=microphone.id_microphone
		INNER JOIN sampling ON catalogue.id_sampling=sampling.id_sampling
		INNER JOIN habitat ON catalogue.id_habitat=habitat.id_habitat
		INNER JOIN municipality ON catalogue.id_municipality=municipality.id_municipality
		INNER JOIN department ON catalogue.id_department=department.id_department
		LEFT OUTER JOIN labeled ON record.id_record=labeled.id_record
		LEFT OUTER JOIN label ON labeled.id_label=label.id_label
		LEFT OUTER JOIN type ON label.id_type=type.id_type
		LEFT OUTER JOIN evidence ON labeled.id_evidence=evidence.id_evidence
		LEFT OUTER JOIN software ON labeled.id_software=software.id_software
		
		-- Filtrado
		where municipality.description = (CASE WHEN municipio IS NOT NULL THEN municipio ELSE municipality.description END) 
		and   catalogue.description = (CASE WHEN catalogo IS NOT NULL THEN catalogo ELSE catalogue.description END)
		and   habitat.description = (CASE WHEN habitat_q IS NOT NULL THEN habitat_q ELSE habitat.description END)
		--and   type.description = (CASE WHEN evento_q IS NOT NULL THEN evento_q ELSE type.description END)
		and   "case".description = (CASE WHEN tipo_case IS NOT NULL THEN tipo_case ELSE "case".description END)
		and   microphone.description = (CASE WHEN tipo_micro IS NOT NULL THEN tipo_micro ELSE microphone.description END)
		--and   evidence.description = (CASE WHEN metodo_etiquetado IS NOT NULL THEN metodo_etiquetado ELSE evidence.description END)
		--and   software.descripton = (CASE WHEN software_q IS NOT NULL THEN software_q ELSE software.descripton END)
		--and   hardware.description = (CASE WHEN tipo_grabadora IS NOT NULL THEN tipo_grabadora ELSE hardware.description END)
		;
end;$$
-------------------------------------------------------------------------------
SELECT label.id_label, label.id_type, label.description, type.description
FROM bioacustica.label
INNER JOIN bioacustica.type ON bioacustica.type.id_type=bioacustica.label.id_type;

SELECT * FROM bioacustica.get_join ('CATALOGO1');
bioacustica
SHOW SEARCH_PATH;
SET SEARCH_PATH TO DEFAULT;
SET SEARCH_PATH TO bioacustica;
---------------------------------------------------------------------------------
id_record
formato
chunk
fecha_record
catalogo
chunks
tipo de grabadora
case
microphone
sampling_description
habitat
ciudad
departamento
elevation
evento = type
metodo de etiquetado
software de etiquetado
nombre del audio no existe agregar
-----------------------------------------------------------------
catalogo varchar default NULL, 
ciudad varchar default NULL,
habitat varchar default NULL,
municipio varchar default NULL,
evento varchar default NULL, == type
tipo_case varchar default NULL,
tipo_micro varchar default NULL,
metodo_etiquetado varchar default NULL,
software varchar default NULL,                   CORREGIR NAME
tipo de grabadora varchar default NULL
fecha min max
elevation min max
-------------------------------------------------------------------
filtro de asignacion de permisos
hablar con Santiago del nombre que dijo alejo