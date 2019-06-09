CREATE TABLE tb_usuario
(
  id_user  SERIAL PRIMARY KEY NOT NULL, 
  idade integer,
  user_name character varying(255),
  nome_user character varying(255),
  senha character varying(255),
  email character varying(255)
);
