-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 09-02-2024 a las 01:16:57
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `softgi`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carritoventas`
--

CREATE TABLE `carritoventas` (
  `contador` int(11) NOT NULL,
  `id_producto` int(11) DEFAULT NULL,
  `nombre_producto` varchar(56) DEFAULT NULL,
  `precio_venta` float DEFAULT NULL,
  `cantidad_adquirida` int(11) DEFAULT NULL,
  `total` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `carritoventas`
--

INSERT INTO `carritoventas` (`contador`, `id_producto`, `nombre_producto`, `precio_venta`, `cantidad_adquirida`, `total`) VALUES
(10, 123233, 'probando', 250, 1, 250),
(11, 632737, 'tornillos', 200, 1, 200),
(12, 123233, 'probando', 250, 1, 250);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categorias`
--

CREATE TABLE `categorias` (
  `id_categoria` int(3) NOT NULL,
  `nom_categoria` varchar(50) DEFAULT NULL,
  `fechahora_creacion` datetime NOT NULL,
  `documento_operador` varchar(10) NOT NULL,
  `nombre_operador` varchar(25) NOT NULL,
  `apellido_operador` varchar(25) NOT NULL,
  `estado_categorias` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `categorias`
--

INSERT INTO `categorias` (`id_categoria`, `nom_categoria`, `fechahora_creacion`, `documento_operador`, `nombre_operador`, `apellido_operador`, `estado_categorias`) VALUES
(1, 'parabrisas', '2023-09-27 23:41:14', '94447540', '', '', 'activo'),
(2, 'Manijas', '2023-10-03 01:31:55', '94447540', 'Eduar', 'Corrales', 'ACTIVO'),
(3, 'chapas', '2023-10-03 01:31:55', '94447540', 'Eduar', 'Corrales', 'ACTIVO'),
(4, 'empaques', '2023-10-03 01:33:37', '94447540', 'Eduar', 'Corrales', 'ACTIVO'),
(5, 'eleva vidrio', '2023-10-03 01:33:37', '94447540', 'Eduar', 'Corrales', 'ACTIVO'),
(6, 'PC', '2023-10-18 20:19:00', '94447540', 'Eduar', 'Corrales', 'INACTIVO'),
(7, 'motor llimpia parabrisas', '2024-02-03 16:04:58', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
(8, 'vidrio puerta toyota hilux', '2024-02-05 10:57:49', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `doc_cliente` varchar(10) NOT NULL,
  `nom_cliente` varchar(56) DEFAULT NULL,
  `ape_cliente` varchar(25) DEFAULT NULL,
  `fecha_nacimiento_cliente` date NOT NULL,
  `contacto_cliente` varchar(10) DEFAULT NULL,
  `email_cliente` varchar(56) DEFAULT NULL,
  `direccion_cliente` varchar(56) DEFAULT NULL,
  `ciudad_cliente` varchar(14) NOT NULL,
  `tipo_persona` varchar(9) DEFAULT NULL,
  `fechahora_registro` datetime NOT NULL,
  `documento_operador` varchar(10) NOT NULL,
  `nombre_operador` varchar(25) NOT NULL,
  `apellido_operador` varchar(25) NOT NULL,
  `estado_cliente` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`doc_cliente`, `nom_cliente`, `ape_cliente`, `fecha_nacimiento_cliente`, `contacto_cliente`, `email_cliente`, `direccion_cliente`, `ciudad_cliente`, `tipo_persona`, `fechahora_registro`, `documento_operador`, `nombre_operador`, `apellido_operador`, `estado_cliente`) VALUES
('1213145566', 'Nicol Maria sebastian', 'Velasco Posada', '1981-09-28', '3155127771', 'nicoafpos@gmail.com', 'Tulua Centro', 'Tulua ', 'natural', '0000-00-00 00:00:00', '16385007', 'Hernan', 'Corrales', 'ACTIVO'),
('1616161616', 'cliente1', 'clientecliente', '2004-09-28', '3171717172', 'cliente1@gmail.com', 'cra1nb#aurescity', 'buguita', 'natural', '2023-09-26 05:02:11', '1112388921', '', '', 'INACTIVO'),
('1818181818', 'felipe', 'Velasco Posada', '2004-09-28', '3161616161', 'velasco@gmail.com', 'cra12#45-70', 'Buga', 'juridica', '0000-00-00 00:00:00', '1112388921', '', '', 'INACTIVO'),
('1919191919', 'cliente3', 'cliente3', '0000-00-00', '3161616161', 'cliente3@gmail.com', 'cra4#21-62', 'Buga', 'natural', '0000-00-00 00:00:00', '1112388921', '', '', 'INACTIVO'),
('26262626', 'NICOL', 'ICOL', '2004-09-28', '123456987', 'DAHYA@GMAILXOM', 'CRA56#5455', 'BIHA', '', '2023-10-18 20:13:20', '94447540', 'Eduar', 'Corrales', 'INACTIVO'),
('33750742', 'kelly', 'Garzon Velasquez', '2024-02-12', '3186941522', 'kelly@gmail.com', 'diagonal 13 # 11-22', 'Bogota', 'natural', '2024-02-03 15:27:15', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
('33750747', 'Adan', 'Segundo', '2002-02-09', '3005667744', 'adan@hotmail.com', 'diagonal 23 # 45-66', 'Tulua', 'juridica', '2024-02-05 15:54:25', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
('44337765', 'Antanas ', 'Mocus Urrego', '2024-02-16', '3122214455', 'juanafvela@gmail.com', 'calle 13a #13-11', 'Cartagena', 'natural', '2024-02-02 20:12:27', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `comprasproveedores`
--

CREATE TABLE `comprasproveedores` (
  `num_compra` int(6) NOT NULL,
  `proveedor_compra` varchar(10) NOT NULL,
  `documento_operador` varchar(10) NOT NULL,
  `nombre_operador` varchar(25) NOT NULL,
  `apellido_operador` varchar(25) NOT NULL,
  `date_compra` datetime NOT NULL,
  `num_factura_proveedor` varchar(10) NOT NULL,
  `estado` varchar(8) NOT NULL,
  `codigo_tabla` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `comprasproveedores`
--

INSERT INTO `comprasproveedores` (`num_compra`, `proveedor_compra`, `documento_operador`, `nombre_operador`, `apellido_operador`, `date_compra`, `num_factura_proveedor`, `estado`, `codigo_tabla`) VALUES
(1, '1133445560', '94447540', 'Eduar', 'Corrales', '2023-10-18 18:52:18', '', 'CANCELAD', ''),
(2, '1133445566', '94447540', 'Eduar', 'Corrales', '2023-10-18 18:52:53', '', 'CANCELAD', ''),
(3, '1133445569', '94447540', 'Eduar', 'Corrales', '2023-10-18 18:54:55', '', 'CANCELAD', ''),
(4, '1133445566', '94447540', 'Eduar', 'Corrales', '2023-10-18 18:57:57', '', 'CANCELAD', ''),
(5, '1133445566', '94447540', 'Eduar', 'Corrales', '2023-10-18 18:58:29', '', 'CANCELAD', ''),
(6, '1133445566', '94447540', 'Eduar', 'Corrales', '2023-10-18 18:59:43', '', 'CANCELAD', ''),
(7, '1133445566', '94447540', 'Eduar', 'Corrales', '2023-10-18 19:00:38', '', 'CANCELAD', ''),
(8, '1133445566', '94447540', 'Eduar', 'Corrales', '2023-10-18 19:00:59', '', 'CANCELAD', ''),
(9, '1133445560', '94447540', 'Eduar', 'Corrales', '2023-10-18 19:02:25', '', 'CANCELAD', ''),
(10, '11338787', '94447540', 'Eduar', 'Corrales', '2023-10-18 19:06:39', '', 'CANCELAD', ''),
(11, '11338787', '94447540', 'Eduar', 'Corrales', '2023-10-18 19:07:21', '', 'CANCELAD', ''),
(12, '1717171717', '94447540', 'Eduar', 'Corrales', '2023-10-18 19:11:48', '', 'CANCELAD', ''),
(13, '1717171717', '94447540', 'Eduar', 'Corrales', '2023-10-18 19:12:18', '', 'CANCELAD', ''),
(14, '1717171717', '94447540', 'Eduar', 'Corrales', '2023-10-18 19:12:32', '', 'CANCELAD', ''),
(15, '1717171717', '94447540', 'Eduar', 'Corrales', '2023-10-18 19:14:51', '', 'CANCELAD', ''),
(16, '1133445569', '94447540', 'Eduar', 'Corrales', '2023-10-18 19:22:26', '', 'CANCELAD', ''),
(17, '1133445560', '94447540', 'Eduar', 'Corrales', '2023-10-18 19:50:31', '', 'CANCELAD', ''),
(18, '1133445560', '94447540', 'Eduar', 'Corrales', '2023-10-18 19:51:33', '', 'CANCELAD', ''),
(19, '1133445560', '94447540', 'Eduar', 'Corrales', '2023-10-18 19:53:14', '', 'CANCELAD', ''),
(20, '1133445566', '94447540', 'Eduar', 'Corrales', '2023-10-18 19:53:58', '', 'CANCELAD', ''),
(21, '02020202', '94447540', 'Eduar', 'Corrales', '2023-10-18 19:56:40', '', 'CANCELAD', ''),
(22, '1133445560', '94447540', 'Eduar', 'Corrales', '2023-11-10 20:13:56', '', 'CANCELAD', 'WpPhz8lgcB'),
(23, '1133445566', '94447540', 'Eduar', 'Corrales', '2023-11-10 20:17:21', '', 'CANCELAD', 'bapP58JRXG'),
(24, '1133445566', '94447540', 'Eduar', 'Corrales', '2023-11-10 20:24:00', '', 'CANCELAD', 'Mbs0INpyRG'),
(25, '1133445560', '94447540', 'Eduar', 'Corrales', '2023-11-10 20:25:59', '', 'CANCELAD', 'xA9KYPSWvz'),
(26, '1133445569', '94447540', 'Eduar', 'Corrales', '2023-11-10 20:27:06', '', 'CANCELAD', 'qe2arhN3Uy'),
(27, '1717171717', '94447540', 'Eduar', 'Corrales', '2023-11-10 20:32:35', '', 'CANCELAD', 'm7tb6X5gd0'),
(28, '1133445560', '94447540', 'Eduar', 'Corrales', '2023-11-10 20:35:55', '', 'CANCELAD', 'WSIQjp7CLc'),
(29, '11338787', '94447540', 'Eduar', 'Corrales', '2023-11-10 20:38:27', '', 'CANCELAD', 'TG27xNs53l'),
(30, '1133445566', '94447540', 'Eduar', 'Corrales', '2023-11-10 20:52:05', '', 'CANCELAD', 'SdBJK5HGF9'),
(31, '1133445569', '94447540', 'Eduar', 'Corrales', '2023-11-10 20:54:39', '', 'ACTIVO', 'Plw2SuqtCD'),
(32, '11338787', '1086358507', 'dennis', 'echeverri', '2023-11-14 19:04:59', '', 'ACTIVO', 'lx3fgq02sd');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cotizaciones`
--

CREATE TABLE `cotizaciones` (
  `num_cotizacion` int(6) NOT NULL,
  `cliente_cotizacion` varchar(10) NOT NULL,
  `documento_operador` varchar(10) NOT NULL,
  `nombre_operador` varchar(25) NOT NULL,
  `apellido_operador` varchar(25) NOT NULL,
  `fecha_inicio_cotizacion` date NOT NULL,
  `fecha_fin_cotizacion` date NOT NULL,
  `nombre_cliente_cotizacion` varchar(50) DEFAULT NULL,
  `estado` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cotizaciones`
--

INSERT INTO `cotizaciones` (`num_cotizacion`, `cliente_cotizacion`, `documento_operador`, `nombre_operador`, `apellido_operador`, `fecha_inicio_cotizacion`, `fecha_fin_cotizacion`, `nombre_cliente_cotizacion`, `estado`) VALUES
(1, '1213145566', '193838362', 'Edixon', 'Payan', '2023-10-26', '2024-12-05', 'cliente1', 'ACTIVO'),
(9, '1213145566', '94447540', 'Eduar', 'Corrales', '2023-10-10', '2023-10-27', 'Nicol ', 'ACTIVO');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detallecomprasproveedores`
--

CREATE TABLE `detallecomprasproveedores` (
  `id_detalle_compra` int(6) NOT NULL,
  `detallenum_compra` int(6) NOT NULL,
  `producto_compra` varchar(6) DEFAULT NULL,
  `cantidad_producto_compra` int(6) NOT NULL,
  `valorunidad_prodcompra` float NOT NULL,
  `valortotal_cantidadcomp` float NOT NULL,
  `totalpagar_compra` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `detallecomprasproveedores`
--

INSERT INTO `detallecomprasproveedores` (`id_detalle_compra`, `detallenum_compra`, `producto_compra`, `cantidad_producto_compra`, `valorunidad_prodcompra`, `valortotal_cantidadcomp`, `totalpagar_compra`) VALUES
(3, 3, 'wdwddw', 34, 3400, 3.40282e38, 0),
(5, 2, 'nose', 3, 56, 565656, 0),
(6, 1, 'otro n', 32, 40000, 3.40282e38, 0),
(7, 10, 'prueb', 3, 43433, 434334000000000, 0),
(9, 12, 'prueba', 3, 3, 333, 0),
(10, 12, 'parabr', 23, 350000, 3.40282e38, 0),
(11, 3, 'prueba', 4, 4, 4444, 0),
(12, 1, 'NIKE', 66, 150000, 3.40282e38, 0),
(13, 2, 'fghfd', 44, 352533, 3.40282e38, 0),
(20, 31, 'vidrio', 43, 2345, 3.40282e38, 0),
(21, 32, 'Pilas', 21, 300000, 3.40282e38, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detallecotizaciones`
--

CREATE TABLE `detallecotizaciones` (
  `id_detalle_cotizacion` int(6) NOT NULL,
  `num_cotizacion` int(6) NOT NULL,
  `producto_cotizacion` varchar(6) DEFAULT NULL,
  `nombre_producto` int(56) NOT NULL,
  `cantidad_productos_cotizacion` int(3) NOT NULL,
  `valorunidad_prodcotizacion` float NOT NULL,
  `valortotal_cantidaproductos_cotizacion` float NOT NULL,
  `servicio_cotizacion` int(6) NOT NULL,
  `cantidad_servicios_cotizacion` int(2) NOT NULL,
  `valorunidad_servicioscotizacion` float NOT NULL,
  `valortotal_cantidadservicios_cotizacion` float NOT NULL,
  `totalpagar_cotizacion` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `detallecotizaciones`
--

INSERT INTO `detallecotizaciones` (`id_detalle_cotizacion`, `num_cotizacion`, `producto_cotizacion`, `nombre_producto`, `cantidad_productos_cotizacion`, `valorunidad_prodcotizacion`, `valortotal_cantidaproductos_cotizacion`, `servicio_cotizacion`, `cantidad_servicios_cotizacion`, `valorunidad_servicioscotizacion`, `valortotal_cantidadservicios_cotizacion`, `totalpagar_cotizacion`) VALUES
(1, 1, '123233', 0, 1, 430, 67, 200, 230, 539, 56, 58),
(2, 1, '123233', 0, 1, 430, 6743, 200, 230, 539, 56, 58),
(5, 1, '632737', 0, 32, 645, 323, 421, 42, 4211, 34234, 43213),
(6, 1, '474747', 0, 76, 2000, 3500, 789, 1, 45000, 45000, 200000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalledevoluciones`
--

CREATE TABLE `detalledevoluciones` (
  `id_detalle_devolucion` int(6) NOT NULL,
  `num_devolucion` int(6) NOT NULL,
  `producto_devolucion` varchar(6) DEFAULT NULL,
  `cantidad_proddevolucion` int(2) DEFAULT NULL,
  `precio_proddevolucion` float DEFAULT NULL,
  `motivo_devolucion` varchar(56) DEFAULT NULL,
  `monto_total_devolucion` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detalleventas`
--

CREATE TABLE `detalleventas` (
  `id_detalle_factura` int(6) NOT NULL,
  `num_factura_venta` int(6) NOT NULL,
  `producto_factura` varchar(200) DEFAULT NULL,
  `cantidad_productos_factura` int(3) NOT NULL,
  `precio_productofactura` float NOT NULL,
  `valortotal_productos_factura` float NOT NULL,
  `servicio_factura` int(6) NOT NULL,
  `cantidad_servicios_factura` int(2) NOT NULL,
  `precio_serviciosfactura` float NOT NULL,
  `valortotal_servicios_factura` float NOT NULL,
  `total_pagar_factura` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `detalleventas`
--

INSERT INTO `detalleventas` (`id_detalle_factura`, `num_factura_venta`, `producto_factura`, `cantidad_productos_factura`, `precio_productofactura`, `valortotal_productos_factura`, `servicio_factura`, `cantidad_servicios_factura`, `precio_serviciosfactura`, `valortotal_servicios_factura`, `total_pagar_factura`) VALUES
(1, 5, 'tornil', 2, 0, 450, 0, 0, 0, 0, 450),
(2, 6, 'tornil', 3, 0, 502, 0, 0, 0, 0, 502),
(3, 7, 'tornil', 2, 0, 450, 0, 0, 0, 0, 450),
(4, 8, 'tornil', 2, 0, 450, 0, 0, 0, 0, 450),
(5, 9, 'proban', 1, 0, 250, 0, 0, 0, 0, 250),
(6, 10, 'proban', 2, 0, 450, 0, 0, 0, 0, 450),
(7, 11, 'tornil', 3, 0, 902, 0, 0, 0, 0, 902),
(8, 12, 'probando, tornillos, probando', 3, 0, 700, 0, 0, 0, 0, 700),
(9, 13, 'probando, tornillos, probando', 3, 0, 700, 0, 0, 0, 0, 700);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `devoluciones`
--

CREATE TABLE `devoluciones` (
  `id_devolucion` int(6) NOT NULL,
  `num_factura` int(6) NOT NULL,
  `documento_operador` varchar(10) NOT NULL,
  `nombre_operador` varchar(25) NOT NULL,
  `apellido_operador` varchar(25) NOT NULL,
  `cliente_devolucion` varchar(10) NOT NULL,
  `fecha_devolucion` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

CREATE TABLE `empleados` (
  `doc_empleado` varchar(10) NOT NULL,
  `nom_empleado` varchar(25) DEFAULT NULL,
  `ape_empleado` varchar(25) DEFAULT NULL,
  `fecha_nacimiento_empleado` date NOT NULL,
  `contacto_empleado` varchar(10) DEFAULT NULL,
  `email_empleado` varchar(56) DEFAULT NULL,
  `direccion_empleado` varchar(56) NOT NULL,
  `ciudad_empleado` varchar(14) NOT NULL,
  `contrasena` varchar(512) DEFAULT NULL,
  `rol` varchar(14) DEFAULT NULL,
  `huelladactilar` blob DEFAULT NULL,
  `fechahora_registroempleado` datetime NOT NULL,
  `documento_operador` varchar(10) NOT NULL,
  `nombre_operador` varchar(25) NOT NULL,
  `apellido_operador` varchar(25) NOT NULL,
  `estado` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleados` (`doc_empleado`, `nom_empleado`, `ape_empleado`, `fecha_nacimiento_empleado`, `contacto_empleado`, `email_empleado`, `direccion_empleado`, `ciudad_empleado`, `contrasena`, `rol`, `huelladactilar`, `fechahora_registroempleado`, `documento_operador`, `nombre_operador`, `apellido_operador`, `estado`) VALUES
('1086358507', 'dennis', 'echeverri', '2023-11-17', '3006888872', 'dennisecheverri46@gmail.com', 'Cajuijio', 'pasto', 'a459867974f1bcc8fc7f1ef07d6373355cfeba01241778822f09127726073b5d98daeb5fc174861fbd2738de2c535d78abe92249e04abb6e7a3bb7b75f98e3b5', ' administrado', NULL, '2023-11-14 18:30:07', '', '', '', 'ACTIVO'),
('1111035245', 'Herney', 'Grisalez', '2024-02-15', '3041144554', 'herney@gamil.com', 'Calle 21 #4-09', 'Buga', '3627909a29c31381a071ec27f7c9ca97726182aed29a7ddd2e54353322cfb30abb9e3a6df2ac2c20fe23436311d678564d0c8d305930575f60e2d3d048184d79', 'vendedor', NULL, '2024-02-02 20:22:10', '', '', '', 'ACTIVO'),
('1112388921', 'Nicol', 'Motoa', '0000-00-00', NULL, 'dahyanna.me@gmail.com', '', '', '3b1c2ae69435c86e2982ab43b8e580b4041c67ff7c1717a0f508a958ce0dba52320c2373b77212cbdd5c8302b4498121fc6fd28da611382b94684e2d9085b591', ' administrador', NULL, '0000-00-00 00:00:00', '', '', '', 'ACTIVO'),
('16161616', 'Andres', 'Velasco', '1970-12-19', '3003003003', 'afvelasco@gmail.com', 'Calle 6 # 6-6', 'Buga', 'Abcde+12345', ' administrador', NULL, '2023-10-26 19:39:44', '', '', '', 'ACTIVO'),
('16385007', 'Hernan', 'Corrales Grisalez', '1981-09-04', '3122175402', 'edcorgriz@hotmail.com', 'Carrera 8 #13-11', '', '3627909a29c31381a071ec27f7c9ca97726182aed29a7ddd2e54353322cfb30abb9e3a6df2ac2c20fe23436311d678564d0c8d305930575f60e2d3d048184d79', 'administrador', NULL, '2023-12-26 17:23:47', '', '', '', 'ACTIVO'),
('193838362', 'Edixon', 'Payan', '2003-03-28', '3162532732', 'edixonpayan5@gmail.com', 'barrio tamarindo calle 1 #24-65', 'buga', 'Ed123456789@', ' administrador', NULL, '2023-10-09 09:13:44', '', '', '', 'ACTIVO'),
('312244556', 'Nicol de De', 'Sebas2', '2004-09-28', '316553344', 'nicolmotoa.28@gmail.com', 'Carrera 33 # 66-66', '', '3627909a29c31381a071ec27f7c9ca97726182aed29a7ddd2e54353322cfb30abb9e3a6df2ac2c20fe23436311d678564d0c8d305930575f60e2d3d048184d79', '', NULL, '2023-12-26 19:25:03', '', '', '', 'ACTIVO'),
('94447540', 'Eduar', 'Corrales', '0000-00-00', NULL, 'edcorgris@gmail.com', '', '', '394919744eb6de1aee9a0fa0fa4330f9c13db999379f93b5e4ae7dd5e715972d90b3920213c52a0f24acb8675321a865aef38146cb2f2ce0e30952f10321ea61', ' administrador', NULL, '0000-00-00 00:00:00', '', '', '', 'ACTIVO');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historial_credito`
--

CREATE TABLE `historial_credito` (
  `contador` int(11) NOT NULL,
  `contador_ventacredito` int(11) DEFAULT NULL,
  `abono` int(11) DEFAULT NULL,
  `operador` int(11) DEFAULT NULL,
  `fecha_abono` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `parametrizacion`
--

CREATE TABLE `parametrizacion` (
  `nom_empresa` varchar(150) DEFAULT NULL,
  `nit_empresa` varchar(10) NOT NULL,
  `logo` varchar(56) DEFAULT NULL,
  `color_empresa` varchar(10) DEFAULT NULL,
  `tipoletra_empresa` varchar(20) DEFAULT NULL,
  `redsocial` varchar(20) DEFAULT NULL,
  `contacto_empresa` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `id_producto` int(6) NOT NULL,
  `ref_produ_1` varchar(50) NOT NULL,
  `ref_produ_2` varchar(50) NOT NULL,
  `ref_produ_3` varchar(50) NOT NULL,
  `categoria` int(3) NOT NULL,
  `nom_categoria` varchar(50) NOT NULL,
  `proveedor` varchar(10) NOT NULL,
  `nom_proveedor` varchar(150) NOT NULL,
  `nombre_producto` varchar(56) NOT NULL,
  `precio_compra` float NOT NULL,
  `precio_venta` float NOT NULL,
  `cantidad_producto` int(4) NOT NULL,
  `descripcion` varchar(250) NOT NULL,
  `stockminimo` int(2) NOT NULL,
  `ubicacion` varchar(8) NOT NULL,
  `estante` int(4) NOT NULL,
  `fechahora_registro` datetime NOT NULL,
  `documento_operador` varchar(10) NOT NULL,
  `nombre_operador` varchar(25) NOT NULL,
  `apellido_operador` varchar(25) NOT NULL,
  `estado_producto` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`id_producto`, `ref_produ_1`, `ref_produ_2`, `ref_produ_3`, `categoria`, `nom_categoria`, `proveedor`, `nom_proveedor`, `nombre_producto`, `precio_compra`, `precio_venta`, `cantidad_producto`, `descripcion`, `stockminimo`, `ubicacion`, `estante`, `fechahora_registro`, `documento_operador`, `nombre_operador`, `apellido_operador`, `estado_producto`) VALUES
(474747, 'manija original renault', 'mani renault 2000', 'lista', 2, 'Manijas', '1133445560', 'Posad FVELA', 'manija', 25, 52, 50, 'fjoierfjajflas', 10, 'Bodega', 7, '2023-10-18 20:22:17', '94447540', 'Eduar', 'Corrales', 'ACTIVO'),
(6327372, 'mot lim kia', 'mot lim kia rio', 'mot lim kia space', 3, 'motor llimpia parabrisas kia', '1133445566', 'oto', 'motor limpia parabrisas kia', 120000, 180000, 640, 'motor limpia parabrisas marca kia todos los modelos del 2022-2024', 10, 'Bodega', 66, '2023-10-03 12:28:50', '94447540', 'Eduar', 'Corrales', 'ACTIVO'),
(12323334, 'udhs', '', '', 1, '', '1133445560', '', 'probando', 200, 250, 4, 'algo nuevo', 3, '1', 3, '2023-10-03 12:19:48', '94447540', 'Eduar', 'Corrales', 'ACTIVO'),
(12323335, 'parabrisa kia sportage', 'parabrisa kia rio', 'parabrisa kia ', 1, 'parabrisas', '02020202', 'oto', 'parabrisas kia', 200000, 300000, 70, 'Prabrisas Kia sportage, rio, soul modelo 2016-2024', 4, 'Bodega', 8, '2024-01-22 16:28:15', '16385007', 'Hernan', 'Corrales', 'ACTIVO'),
(12323336, 'empaque puerta delantera ford', 'empaque puerta dodge', 'empaque puerta chevrolet', 4, 'empaques', '1717171717', 'Prueba1', 'Empaque puerta delanteras', 350000, 450000, 300, 'Empaque para puerta doble canal original ford', 30, 'Bodega', 5, '2024-01-24 20:37:48', '16385007', 'Hernan', 'Corrales', 'ACTIVO'),
(12323338, '94477540', '23f', '24r', 1, 'parabrisas', '02020202', 'oto', 'parabrisas GMC', 12000, 140000, 40, 'parabrias GMC modelo 2000-2023', 2, 'Bodega', 1, '2024-02-01 19:38:35', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
(12323339, 'parab1', 'parab2', 'parab3', 1, 'parabrisas', '1133445566', 'AFV ECHEVERI', 'parabrisas GT Ford', 120000, 150000, 20, 'parabrisas para Ford Gt', 2, 'Bodega', 2, '2024-02-02 16:09:01', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
(12323340, '1PCBA\'U01\'S07ZAR', '94477540', 'Q1', 2, 'Manijas', '1717171717', 'Prueba1', 'manija hiunday', 10000, 150000, 40, 'manija hiunday original', 4, 'Almacen', 3, '2024-02-02 19:15:30', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
(12323341, '97895856771669786073133333', '9786073133333', '2PD', 3, 'chapas', '11338787', 'Posad FVELASCO', 'chapas puertas traseras chery q', 30000, 50000, 60, 'chapa chery q puertas traseras lado derecho', 3, 'Bodega', 34, '2024-02-02 19:20:35', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
(12323342, 'chapa rb24', 'chapa chery qrb', 'chapa chevrolet rb', 3, 'chapas', '02020202', 'oto', 'chapa derecha trasera chery y chevrolet', 35000, 55000, 60, 'chapa puerta trasera derecha para chery chevrolet modelo 2020-2024', 10, 'Bodega', 45, '2024-02-02 19:24:45', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
(12323343, '2PDCN', '1PCBA\'U01\'S07ZAR', '94477540eh', 1, 'parabrisas', '02020202', 'oto', 'Empaque puerta doble canal Renault', 20000, 33000, 30, 'Empaque para puerta doble canal original ford', 2, 'Bodega', 2, '2024-02-02 20:03:17', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
(12323344, 'motor limpia parabrisas chevrolet', 'motor limpia parabrisas chery', 'motor gm', 7, 'motor llimpia parabrisas', '1717171717', 'Prueba1', 'motor limpia parabrisas para chevrolet', 150000, 200000, 60, 'motor limpia parabrisas para chevrolet, chery modelos 2010-2024', 4, 'Bodega', 5, '2024-02-05 08:29:44', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
(12323345, '864904050363710', '31802-k2qu00633', '77024411', 3, 'chapas', '1133445560', 'Posad FVELA', 'Chapa de seguridad Sandero', 50000, 1000, 20, 'jlksjf lkasj lk alskdjkasljl', 2, 'Bodega', 0, '2024-02-05 20:28:49', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
(12323346, 'motor limpia parabrisas chevrolet', 'Motor chevy 111', 'motor chevrolet', 7, 'motor llimpia parabrisas', '1133445566', 'AFV ECHEVERI', 'motor limpia parabrisas para chevrolet', 100, 70, 30, 'motor limpia parabrisas para chevrolet, chery modelos 2010-2024', 40, 'Bodega', 4, '2024-02-08 16:00:32', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
(12323347, ' motor limpia parabrisas chevrolet', 'motor limpia parabrisas chery', 'motor gm', 7, 'motor llimpia parabrisas', '2323232323', 'DAHYANNA', 'motor limpia parabrisas para chevrolet', 100, 140, 30, 'motor limpia parabrisas para chevrolet, chery modelos 2010-2024', 10, 'Bodega', 44, '2024-02-08 16:49:30', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proveedores`
--

CREATE TABLE `proveedores` (
  `doc_proveedor` varchar(10) NOT NULL,
  `nom_proveedor` varchar(56) DEFAULT NULL,
  `contacto_proveedor` varchar(10) DEFAULT NULL,
  `email_proveedor` varchar(56) DEFAULT NULL,
  `direccion_proveedor` varchar(56) DEFAULT NULL,
  `ciudad_proveedor` varchar(14) NOT NULL,
  `registro_proveedor` datetime NOT NULL,
  `documento_operador` varchar(10) NOT NULL,
  `nombre_operador` varchar(25) NOT NULL,
  `apellido_operador` varchar(25) NOT NULL,
  `estado_proveedor` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `proveedores`
--

INSERT INTO `proveedores` (`doc_proveedor`, `nom_proveedor`, `contacto_proveedor`, `email_proveedor`, `direccion_proveedor`, `ciudad_proveedor`, `registro_proveedor`, `documento_operador`, `nombre_operador`, `apellido_operador`, `estado_proveedor`) VALUES
('02020202', 'oto', '41414144', 'dfffafafa@gmail.com', 'carrera 14 #34-25', 'Buga', '2023-10-18 19:55:54', '16385007', 'Hernan', 'Corrales Grisalez', 'INACTIVO'),
('1133445560', 'Posad FVELA', '3144455678', 'edccor@hotmail.om', 'Calle 6sur #13b40', 'Cali', '2023-09-27 16:25:22', '1112388921', '', '', 'ACTIVO'),
('1133445566', 'AFV ECHEVERI', '3144455678', 'edccor@hotmail.om', 'Calle 6sur #13b40', 'Cali', '2023-09-27 16:21:41', '1112388921', '', '', 'ACTIVO'),
('1133445569', 'Posad FVELA', '3144455678', 'edccor@hotmail.om', 'Calle 6sur #13b40', 'Cali', '2023-09-27 16:24:34', '1112388921', '', '', 'ACTIVO'),
('1133445570', 'Posad FVELASCO', '3144455678', 'edccor@hotmail.om', 'Calle 6sur #13b40', 'Cali', '2023-09-27 16:26:08', '1112388921', '', '', 'ACTIVO'),
('1133445572', 'AFNICOL', '3144455678', 'edccor@hotmail.om', 'Calle 6sur #13b40', 'Cali', '2023-09-27 16:27:02', '1112388921', '', '', 'ACTIVO'),
('1133872732', 'Posad FVELASCOe', '3144455678', 'edccor@hotmail.om', 'Calle 6sur #13b40', 'Cali', '2023-09-27 16:36:55', '1112388921', '', '', 'ACTIVO'),
('1133872738', 'Posad FVELASCOe', '3144455678', 'edccor@hotmail.om', 'Calle 6sur #13b40', 'Cali', '2023-09-27 16:37:52', '1112388921', '', '', 'ACTIVO'),
('11338787', 'Posad FVELASCO', '3144455678', 'edccor@hotmail.om', 'Calle 6sur #13b40', 'Cali', '2023-09-27 16:27:56', '1112388921', '', '', 'ACTIVO'),
('113387870', 'Posad FVELASCOe', '3144455678', 'edccor@hotmail.om', 'Calle 6sur #13b40', 'Cali', '2023-09-27 16:29:42', '1112388921', '', '', 'ACTIVO'),
('113387871', 'Posad FVELASCO', '3144455678', 'edccor@hotmail.om', 'Calle 6sur #13b40', 'Cali', '2023-09-27 16:33:55', '1112388921', '', '', 'ACTIVO'),
('1133878712', 'Posad FVELASCOe', '3144455678', 'edccor@hotmail.om', 'Calle 6sur #13b40', 'Cali', '2023-09-27 16:34:15', '1112388921', '', '', 'ACTIVO'),
('1133878732', 'Posad FVELASCOe', '3144455678', 'edccor@hotmail.om', 'Calle 6sur #13b40', 'Cali', '2023-09-27 16:35:06', '1112388921', '', '', 'ACTIVO'),
('113387876', 'Posad FVELASCOe', '3144455678', 'edccor@hotmail.om', 'Calle 6sur #13b40', 'Cali', '2023-09-27 16:32:16', '1112388921', '', '', 'ACTIVO'),
('113387879', 'Posad FVELASCOe', '3144455678', 'edccor@hotmail.om', 'Calle 6sur #13b40', 'Cali', '2023-09-27 16:29:12', '1112388921', '', '', 'ACTIVO'),
('1212121212', 'AF Posada S.A.S', '3121212121', 'afproveedor1@gmail.com', 'cra12#bugacity', 'Buga', '2023-09-27 14:33:50', '1112388921', '', '', 'ACTIVO'),
('1515151515', 'afproveedor1', '3151515151', 'proveedor1@gmail.com', 'cra13#bugacity', 'buguita', '2023-09-26 04:59:29', '1112388921', '', '', 'ACTIVO'),
('1717171717', 'Prueba1', '3151515151', 'pruebas@gmail.com', 'cra12#bugacity', 'Buga', '2023-09-27 15:40:17', '1112388921', '', '', 'ACTIVO'),
('2323232323', 'DAHYANNA', '1548796542', 'dahy@gmail.com', 'cra45#45-89', 'BUGA', '2023-10-18 20:12:03', '94447540', 'Eduar', 'Corrales', 'ACTIVO'),
('9345678911', 'AF Posada S.A', '3212122245', 'edccor@hotmail.om', 'carrera 25 #5-10', 'Buga', '2023-09-26 22:24:46', '1112388921', '', '', 'ACTIVO');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `recuperarcontrasena`
--

CREATE TABLE `recuperarcontrasena` (
  `id_solicitud` int(11) NOT NULL,
  `email_usuario` varchar(30) DEFAULT NULL,
  `fechahora_solicitud` datetime DEFAULT NULL,
  `fechahora_termina` datetime DEFAULT NULL,
  `codigo` varchar(52) DEFAULT NULL,
  `usuario` varchar(10) DEFAULT NULL,
  `utilizado` varchar(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `recuperarcontrasena`
--

INSERT INTO `recuperarcontrasena` (`id_solicitud`, `email_usuario`, `fechahora_solicitud`, `fechahora_termina`, `codigo`, `usuario`, `utilizado`) VALUES
(1, 'dennisecheverri46@gmail.com', '2023-11-14 18:34:14', '2023-11-14 18:37:14', 'N007W4JTSuXDiXj2MhvNBSAxrsZ447Ol', '1086358507', 'si'),
(2, 'edcorgris@gmail.com', '2023-12-23 20:36:15', '2023-12-23 20:39:15', '49nLo83UBdzPZcV3ofZ9H9OO785CYuqW', '94447540', 'si');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `servicios`
--

CREATE TABLE `servicios` (
  `nom_servicio` varchar(56) NOT NULL,
  `id_servicio` int(6) NOT NULL,
  `cliente_servicio` varchar(10) NOT NULL,
  `documento_operador` varchar(10) NOT NULL,
  `nombre_operador` varchar(25) NOT NULL,
  `apellido_operador` varchar(25) NOT NULL,
  `precio_servicio` float NOT NULL,
  `fecha_inicio_servicio` date NOT NULL,
  `fecha_fin_servicio` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tokens`
--

CREATE TABLE `tokens` (
  `id_token` int(11) NOT NULL,
  `doc_empleado` varchar(10) NOT NULL,
  `nom_empleado` varchar(25) NOT NULL,
  `email_empleado` varchar(8) NOT NULL,
  `token` varchar(32) NOT NULL,
  `confir_user` varchar(13) NOT NULL,
  `tiempo_registro` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tokens`
--

INSERT INTO `tokens` (`id_token`, `doc_empleado`, `nom_empleado`, `email_empleado`, `token`, `confir_user`, `tiempo_registro`) VALUES
(1, '1112388921', 'Nicol', 'dahyanna', 'e2swBhEiJpsaoeNAggF1sX003H54IowA', 'confirmado', '2023-09-25 21:31:55'),
(2, '94447540', 'Eduar', 'edcorgri', 'qtfQ4Jkg3D0nxrZHVwFY8O4FY3wNptQO', 'confirmado', '2023-09-26 21:34:16'),
(3, '193838362', 'Edixon', 'edixonpa', 'GWsZaDw9nysdBpQrADgpMYIpwbI2rEcD', 'confirmado', '2023-10-09 09:13:44'),
(4, '16161616', 'Andres', 'afvelasc', 'RgrLiyBakuos1PrcseEQ2LLKy7jYX5Pm', 'confirmado', '2023-10-26 19:39:44'),
(5, '1086358507', 'dennis', 'dennisec', '1vxpV69GWcMXkohj7t47OTpmPm4QJuna', 'confirmado', '2023-11-14 18:30:07'),
(17, '16385007', 'Hernan', 'edcorgri', 'X0bNZpY2imxwk9c6fFiY3ACFv2nQ4eaB', 'confirmado', '2023-12-26 17:23:47'),
(23, '312244556', 'Nicol de D', 'nicolmot', 'jCBJvP5wz2yVrPvnTzL2LX6xpEYydObK', 'no confirmado', '2023-12-26 19:25:03'),
(24, '1111035245', 'Herney', 'herney@g', 'y18puDuaGuuunGYhDvivSqx1H9V9TFdE', 'no confirmado', '2024-02-02 20:22:10');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ubicacion`
--

CREATE TABLE `ubicacion` (
  `num_estante` int(11) NOT NULL,
  `almacen` varchar(2) DEFAULT NULL,
  `bodega` varchar(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas`
--

CREATE TABLE `ventas` (
  `num_factura` int(6) NOT NULL,
  `cliente_factura` varchar(10) DEFAULT NULL,
  `numero_cotizacion` int(6) NOT NULL,
  `documento_operador` varchar(10) DEFAULT NULL,
  `nombre_operador` varchar(25) NOT NULL,
  `apellido_operador` varchar(25) NOT NULL,
  `fechahora_venta` datetime DEFAULT NULL,
  `forma_pago` varchar(12) DEFAULT NULL,
  `medio_pago` varchar(7) DEFAULT NULL,
  `codigo_tabla` varchar(20) DEFAULT NULL,
  `operador_factura` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ventas`
--

INSERT INTO `ventas` (`num_factura`, `cliente_factura`, `numero_cotizacion`, `documento_operador`, `nombre_operador`, `apellido_operador`, `fechahora_venta`, `forma_pago`, `medio_pago`, `codigo_tabla`, `operador_factura`) VALUES
(5, '1213145566', 0, NULL, '', '', '2023-11-14 19:33:33', 'efectivo', NULL, '2UKQ3q5Jx1lebk0FwCpa', '1086358507'),
(6, '1213145566', 0, NULL, '', '', '2023-11-14 19:35:16', 'Bancolombia', NULL, 'MQkqNXdh9bjOfLs6Txgz', '1086358507'),
(7, '1213145566', 0, NULL, '', '', '2023-11-14 19:48:03', 'efectivo', NULL, 'tpgz46LK7iHFrNR5qsew', '1086358507'),
(8, '1213145566', 0, NULL, '', '', '2023-11-14 19:51:04', 'efectivo', NULL, '7EQqdNjpMtOlSGz6vY8W', '1086358507'),
(9, '1213145566', 0, NULL, '', '', '2023-11-14 19:51:52', 'efectivo', NULL, '9yWhFX6jVT5HswcQ8El1', '1086358507'),
(10, '1213145566', 0, NULL, '', '', '2023-11-14 19:53:14', 'efectivo', NULL, 'B8yOePEXKY9L6JQCrtVi', '1086358507'),
(11, '1213145566', 0, NULL, '', '', '2023-11-14 19:56:46', 'Daviplata', NULL, 'lPzBGbX7a6oh5uFJtenO', '1086358507'),
(12, '1213145566', 0, NULL, '', '', '2023-11-14 20:01:01', 'efectivo', NULL, '7ND6ZaFqCjokgx0TYMRB', '1086358507'),
(13, '1213145566', 0, NULL, '', '', '2023-11-14 21:28:27', 'Daviplata', NULL, 'T678PMpSVouCKLfUXxRw', '1086358507');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas_credito`
--

CREATE TABLE `ventas_credito` (
  `contador` int(11) NOT NULL,
  `cliente` varchar(10) DEFAULT NULL,
  `productos` varchar(70) DEFAULT NULL,
  `credito_total` int(11) DEFAULT NULL,
  `credito_restante` int(11) DEFAULT NULL,
  `operador` int(11) DEFAULT NULL,
  `fecha_venta` datetime DEFAULT NULL,
  `estado` varchar(9) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ventas_credito`
--

INSERT INTO `ventas_credito` (`contador`, `cliente`, `productos`, `credito_total`, `credito_restante`, `operador`, `fecha_venta`, `estado`) VALUES
(1, '1213145566', 'probando, tornillos, probando', 700, 700, 1086358507, '2023-11-14 21:21:09', 'ACTIVO');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `carritoventas`
--
ALTER TABLE `carritoventas`
  ADD PRIMARY KEY (`contador`);

--
-- Indices de la tabla `categorias`
--
ALTER TABLE `categorias`
  ADD PRIMARY KEY (`id_categoria`),
  ADD KEY `operador_categoria` (`documento_operador`);

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`doc_cliente`),
  ADD KEY `operador` (`documento_operador`);

--
-- Indices de la tabla `comprasproveedores`
--
ALTER TABLE `comprasproveedores`
  ADD PRIMARY KEY (`num_compra`),
  ADD KEY `provcomp` (`proveedor_compra`),
  ADD KEY `operador_compprovee` (`documento_operador`);

--
-- Indices de la tabla `cotizaciones`
--
ALTER TABLE `cotizaciones`
  ADD PRIMARY KEY (`num_cotizacion`),
  ADD KEY `cotclie` (`cliente_cotizacion`),
  ADD KEY `cotempl` (`documento_operador`);

--
-- Indices de la tabla `detallecomprasproveedores`
--
ALTER TABLE `detallecomprasproveedores`
  ADD PRIMARY KEY (`id_detalle_compra`),
  ADD KEY `compra` (`detallenum_compra`),
  ADD KEY `producto` (`producto_compra`);

--
-- Indices de la tabla `detallecotizaciones`
--
ALTER TABLE `detallecotizaciones`
  ADD PRIMARY KEY (`id_detalle_cotizacion`),
  ADD KEY `cot` (`num_cotizacion`),
  ADD KEY `prod` (`producto_cotizacion`);

--
-- Indices de la tabla `detalledevoluciones`
--
ALTER TABLE `detalledevoluciones`
  ADD PRIMARY KEY (`id_detalle_devolucion`),
  ADD KEY `dev` (`num_devolucion`),
  ADD KEY `prod` (`producto_devolucion`);

--
-- Indices de la tabla `detalleventas`
--
ALTER TABLE `detalleventas`
  ADD PRIMARY KEY (`id_detalle_factura`),
  ADD KEY `fac` (`num_factura_venta`);

--
-- Indices de la tabla `devoluciones`
--
ALTER TABLE `devoluciones`
  ADD PRIMARY KEY (`id_devolucion`),
  ADD KEY `factura` (`num_factura`),
  ADD KEY `operador_devolucion` (`documento_operador`),
  ADD KEY `cliente_devolucion` (`cliente_devolucion`);

--
-- Indices de la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`doc_empleado`);

--
-- Indices de la tabla `historial_credito`
--
ALTER TABLE `historial_credito`
  ADD PRIMARY KEY (`contador`);

--
-- Indices de la tabla `parametrizacion`
--
ALTER TABLE `parametrizacion`
  ADD PRIMARY KEY (`nit_empresa`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id_producto`),
  ADD KEY `prov` (`proveedor`),
  ADD KEY `cat` (`categoria`),
  ADD KEY `operador_producto` (`documento_operador`);

--
-- Indices de la tabla `proveedores`
--
ALTER TABLE `proveedores`
  ADD PRIMARY KEY (`doc_proveedor`),
  ADD KEY `operador_proveedor` (`documento_operador`);

--
-- Indices de la tabla `recuperarcontrasena`
--
ALTER TABLE `recuperarcontrasena`
  ADD PRIMARY KEY (`id_solicitud`),
  ADD KEY `usuario` (`usuario`);

--
-- Indices de la tabla `servicios`
--
ALTER TABLE `servicios`
  ADD PRIMARY KEY (`id_servicio`),
  ADD KEY `cliente_servicio` (`cliente_servicio`),
  ADD KEY `operador_servicio` (`documento_operador`);

--
-- Indices de la tabla `tokens`
--
ALTER TABLE `tokens`
  ADD PRIMARY KEY (`id_token`),
  ADD KEY `doc_empleado` (`doc_empleado`);

--
-- Indices de la tabla `ubicacion`
--
ALTER TABLE `ubicacion`
  ADD PRIMARY KEY (`num_estante`);

--
-- Indices de la tabla `ventas`
--
ALTER TABLE `ventas`
  ADD PRIMARY KEY (`num_factura`),
  ADD KEY `facclie` (`cliente_factura`),
  ADD KEY `factempl` (`documento_operador`);

--
-- Indices de la tabla `ventas_credito`
--
ALTER TABLE `ventas_credito`
  ADD PRIMARY KEY (`contador`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `carritoventas`
--
ALTER TABLE `carritoventas`
  MODIFY `contador` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `categorias`
--
ALTER TABLE `categorias`
  MODIFY `id_categoria` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `comprasproveedores`
--
ALTER TABLE `comprasproveedores`
  MODIFY `num_compra` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT de la tabla `cotizaciones`
--
ALTER TABLE `cotizaciones`
  MODIFY `num_cotizacion` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `detallecomprasproveedores`
--
ALTER TABLE `detallecomprasproveedores`
  MODIFY `id_detalle_compra` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT de la tabla `detallecotizaciones`
--
ALTER TABLE `detallecotizaciones`
  MODIFY `id_detalle_cotizacion` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `detalledevoluciones`
--
ALTER TABLE `detalledevoluciones`
  MODIFY `id_detalle_devolucion` int(6) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `detalleventas`
--
ALTER TABLE `detalleventas`
  MODIFY `id_detalle_factura` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `devoluciones`
--
ALTER TABLE `devoluciones`
  MODIFY `id_devolucion` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `historial_credito`
--
ALTER TABLE `historial_credito`
  MODIFY `contador` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id_producto` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12323348;

--
-- AUTO_INCREMENT de la tabla `recuperarcontrasena`
--
ALTER TABLE `recuperarcontrasena`
  MODIFY `id_solicitud` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `servicios`
--
ALTER TABLE `servicios`
  MODIFY `id_servicio` int(6) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tokens`
--
ALTER TABLE `tokens`
  MODIFY `id_token` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT de la tabla `ubicacion`
--
ALTER TABLE `ubicacion`
  MODIFY `num_estante` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `ventas`
--
ALTER TABLE `ventas`
  MODIFY `num_factura` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `ventas_credito`
--
ALTER TABLE `ventas_credito`
  MODIFY `contador` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `categorias`
--
ALTER TABLE `categorias`
  ADD CONSTRAINT `operador_categoria` FOREIGN KEY (`documento_operador`) REFERENCES `empleados` (`doc_empleado`);

--
-- Filtros para la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD CONSTRAINT `operador` FOREIGN KEY (`documento_operador`) REFERENCES `empleados` (`doc_empleado`);

--
-- Filtros para la tabla `comprasproveedores`
--
ALTER TABLE `comprasproveedores`
  ADD CONSTRAINT `comprasproveedores_ibfk_1` FOREIGN KEY (`proveedor_compra`) REFERENCES `proveedores` (`doc_proveedor`),
  ADD CONSTRAINT `operador_compprovee` FOREIGN KEY (`documento_operador`) REFERENCES `empleados` (`doc_empleado`);

--
-- Filtros para la tabla `cotizaciones`
--
ALTER TABLE `cotizaciones`
  ADD CONSTRAINT `cotizaciones_ibfk_1` FOREIGN KEY (`cliente_cotizacion`) REFERENCES `clientes` (`doc_cliente`);

--
-- Filtros para la tabla `detallecomprasproveedores`
--
ALTER TABLE `detallecomprasproveedores`
  ADD CONSTRAINT `detallecomprasproveedores_ibfk_1` FOREIGN KEY (`detallenum_compra`) REFERENCES `comprasproveedores` (`num_compra`);

--
-- Filtros para la tabla `detallecotizaciones`
--
ALTER TABLE `detallecotizaciones`
  ADD CONSTRAINT `detallecotizaciones_ibfk_1` FOREIGN KEY (`num_cotizacion`) REFERENCES `cotizaciones` (`num_cotizacion`);

--
-- Filtros para la tabla `detalledevoluciones`
--
ALTER TABLE `detalledevoluciones`
  ADD CONSTRAINT `detalledevoluciones_ibfk_1` FOREIGN KEY (`num_devolucion`) REFERENCES `devoluciones` (`id_devolucion`);

--
-- Filtros para la tabla `detalleventas`
--
ALTER TABLE `detalleventas`
  ADD CONSTRAINT `detalleventas_ibfk_1` FOREIGN KEY (`num_factura_venta`) REFERENCES `ventas` (`num_factura`);

--
-- Filtros para la tabla `devoluciones`
--
ALTER TABLE `devoluciones`
  ADD CONSTRAINT `cliente_devolucion` FOREIGN KEY (`cliente_devolucion`) REFERENCES `clientes` (`doc_cliente`),
  ADD CONSTRAINT `devoluciones_ibfk_1` FOREIGN KEY (`num_factura`) REFERENCES `ventas` (`num_factura`),
  ADD CONSTRAINT `operador_devolucion` FOREIGN KEY (`documento_operador`) REFERENCES `empleados` (`doc_empleado`);

--
-- Filtros para la tabla `productos`
--
ALTER TABLE `productos`
  ADD CONSTRAINT `operador_producto` FOREIGN KEY (`documento_operador`) REFERENCES `empleados` (`doc_empleado`),
  ADD CONSTRAINT `productos_ibfk_1` FOREIGN KEY (`proveedor`) REFERENCES `proveedores` (`doc_proveedor`),
  ADD CONSTRAINT `productos_ibfk_2` FOREIGN KEY (`categoria`) REFERENCES `categorias` (`id_categoria`);

--
-- Filtros para la tabla `proveedores`
--
ALTER TABLE `proveedores`
  ADD CONSTRAINT `operador_proveedor` FOREIGN KEY (`documento_operador`) REFERENCES `empleados` (`doc_empleado`);

--
-- Filtros para la tabla `recuperarcontrasena`
--
ALTER TABLE `recuperarcontrasena`
  ADD CONSTRAINT `recuperarcontrasena_ibfk_1` FOREIGN KEY (`usuario`) REFERENCES `empleados` (`doc_empleado`);

--
-- Filtros para la tabla `servicios`
--
ALTER TABLE `servicios`
  ADD CONSTRAINT `cliente_servicio` FOREIGN KEY (`cliente_servicio`) REFERENCES `clientes` (`doc_cliente`),
  ADD CONSTRAINT `operador_servicio` FOREIGN KEY (`documento_operador`) REFERENCES `empleados` (`doc_empleado`);

--
-- Filtros para la tabla `tokens`
--
ALTER TABLE `tokens`
  ADD CONSTRAINT `doc_empleado` FOREIGN KEY (`doc_empleado`) REFERENCES `empleados` (`doc_empleado`);

--
-- Filtros para la tabla `ventas`
--
ALTER TABLE `ventas`
  ADD CONSTRAINT `ventas_ibfk_1` FOREIGN KEY (`cliente_factura`) REFERENCES `clientes` (`doc_cliente`),
  ADD CONSTRAINT `ventas_ibfk_2` FOREIGN KEY (`documento_operador`) REFERENCES `empleados` (`doc_empleado`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
