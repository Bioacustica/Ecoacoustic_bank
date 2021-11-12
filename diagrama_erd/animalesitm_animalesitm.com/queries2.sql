create or replace function bioacustica.get_join(etiqueta varchar default NULL) 
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
		INNER JOIN type ON type.id_type=label.id_type
		where label.description = (CASE WHEN etiqueta IS NOT NULL THEN etiqueta ELSE label.description END);
end;$$
-------------------------------------------------------------------------------
SELECT label.id_label, label.id_type, label.description, type.description
FROM label
INNER JOIN type ON type.id_type=label.id_type;

SELECT * FROM bioacustica.get_join ('s');