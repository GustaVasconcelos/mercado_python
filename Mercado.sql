PGDMP         ;            
    z            estoque    15.1    15.0     ?           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            ?           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            ?           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            ?           1262    16421    estoque    DATABASE     ~   CREATE DATABASE estoque WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Portuguese_Brazil.1252';
    DROP DATABASE estoque;
                postgres    false            ?            1259    49193    estoque_produto    TABLE     ?   CREATE TABLE public.estoque_produto (
    id_produto integer NOT NULL,
    nome_produto character varying,
    quantidade_produto integer,
    preco numeric
);
 #   DROP TABLE public.estoque_produto;
       public         heap    postgres    false            ?            1259    49192    estoque_produto_id_produto_seq    SEQUENCE     ?   CREATE SEQUENCE public.estoque_produto_id_produto_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 5   DROP SEQUENCE public.estoque_produto_id_produto_seq;
       public          postgres    false    215            ?           0    0    estoque_produto_id_produto_seq    SEQUENCE OWNED BY     a   ALTER SEQUENCE public.estoque_produto_id_produto_seq OWNED BY public.estoque_produto.id_produto;
          public          postgres    false    214            e           2604    49196    estoque_produto id_produto    DEFAULT     ?   ALTER TABLE ONLY public.estoque_produto ALTER COLUMN id_produto SET DEFAULT nextval('public.estoque_produto_id_produto_seq'::regclass);
 I   ALTER TABLE public.estoque_produto ALTER COLUMN id_produto DROP DEFAULT;
       public          postgres    false    214    215    215            ?          0    49193    estoque_produto 
   TABLE DATA           ^   COPY public.estoque_produto (id_produto, nome_produto, quantidade_produto, preco) FROM stdin;
    public          postgres    false    215   ?       ?           0    0    estoque_produto_id_produto_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.estoque_produto_id_produto_seq', 1, true);
          public          postgres    false    214            g           2606    49200 $   estoque_produto estoque_produto_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.estoque_produto
    ADD CONSTRAINT estoque_produto_pkey PRIMARY KEY (id_produto);
 N   ALTER TABLE ONLY public.estoque_produto DROP CONSTRAINT estoque_produto_pkey;
       public            postgres    false    215            ?      x?3?tK??:?8??Ѐ?Tϔ+F??? I"K     