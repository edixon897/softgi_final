-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 01-04-2024 a las 17:11:39
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
(8, 'vidrio puerta toyota hilux', '2024-02-05 10:57:49', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
(9, 'Miona Chevrolet', '2024-03-19 10:35:06', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO');

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
('1213145566', 'Nicol Maria ', 'Velasco Posada', '1981-09-28', '3155127771', 'nicoafpos@gmail.com', 'Tulua Centro', 'Tulua ', 'natural', '0000-00-00 00:00:00', '1089000896', 'Edixon', 'Payan Hurtado', 'ACTIVO'),
('1616161616', 'Luis esteban', 'pelo pintado', '2004-09-28', '3171717172', 'cliente1@gmail.com', 'cra1nb#aurescity', 'buguita', 'natural', '2023-09-26 05:02:11', '1089000896', 'Edixon', 'Payan Hurtado', 'ACTIVO'),
('1818181818', 'felipe', 'Velasco Posada', '2004-09-28', '3161616161', 'velasco@gmail.com', 'cra12#45-70', 'Buga', 'juridica', '0000-00-00 00:00:00', '1112388921', '', '', 'ACTIVO'),
('1919191919', 'cliente3', 'cliente3', '0000-00-00', '3161616161', 'cliente3@gmail.com', 'cra4#21-62', 'Buga', 'natural', '0000-00-00 00:00:00', '1112388921', '', '', 'ACTIVO'),
('26262626', 'NICOL', 'ICOL', '2004-09-28', '123456987', 'DAHYA@GMAILXOM', 'CRA56#5455', 'BIHA', '', '2023-10-18 20:13:20', '94447540', 'Eduar', 'Corrales', 'ACTIVO'),
('33750742', 'kelly', 'Garzon Velasquez', '2024-02-12', '3186941522', 'kelly@gmail.com', 'diagonal 13 # 11-22', 'Bogota', 'natural', '2024-02-03 15:27:15', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
('33750747', 'Adan', 'Segundo', '2002-02-09', '3005667744', 'adan@hotmail.com', 'diagonal 23 # 45-66', 'Tulua', 'juridica', '2024-02-05 15:54:25', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
('44337765', 'Antanas ', 'Mocus Urrego', '2024-02-16', '3122214455', 'juanafvela@gmail.com', 'calle 13a #13-11', 'Cartagena', 'natural', '2024-02-02 20:12:27', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
('53442612', 'Luis sebastia', 'pelo pintado', '2001-03-21', '352634223', 'luissebastian0@gmail.com', 'carrera 7 #98-76', 'buga', 'juridica', '2024-03-08 09:45:44', '1089000896', 'Edixon', 'Payan Hurtado', 'ACTIVO');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `comprasproveedores`
--

CREATE TABLE `comprasproveedores` (
  `num_compra` int(6) NOT NULL,
  `proveedor_compra` varchar(10) NOT NULL,
  `fecha_compra` date NOT NULL,
  `documento_operador` varchar(10) NOT NULL,
  `nombre_operador` varchar(25) NOT NULL,
  `apellido_operador` varchar(25) NOT NULL,
  `tiempo_registro` datetime NOT NULL,
  `num_factura_proveedor` varchar(10) NOT NULL,
  `estado` varchar(8) NOT NULL,
  `codigo_tabla` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `comprasproveedores`
--

INSERT INTO `comprasproveedores` (`num_compra`, `proveedor_compra`, `fecha_compra`, `documento_operador`, `nombre_operador`, `apellido_operador`, `tiempo_registro`, `num_factura_proveedor`, `estado`, `codigo_tabla`) VALUES
(63, '1133445566', '2024-03-29', '16385007', 'Hernan', 'Corrales Grisalez', '2024-03-31 18:00:56', '0100', 'ACTIVO', '7NU8TJFKYT'),
(64, '1133445570', '2024-03-28', '16385007', 'Hernan', 'Corrales Grisalez', '2024-03-31 18:24:41', '0033', 'ACTIVO', '2FK08MZHVH'),
(65, '1133445572', '2024-03-29', '16385007', 'Hernan', 'Corrales Grisalez', '2024-03-31 23:23:35', '003', 'ACTIVO', '2TF30OAJC4'),
(66, '2323232323', '2024-03-29', '16385007', 'Hernan', 'Corrales Grisalez', '2024-03-31 23:24:35', '004', 'ACTIVO', 'FT3HYK5XUL'),
(67, '1133445570', '2024-03-29', '16385007', 'Hernan', 'Corrales Grisalez', '2024-03-31 23:46:38', '005', 'ACTIVO', 'O2Q087Q2YL'),
(68, '1717171717', '2024-03-30', '16385007', 'Hernan', 'Corrales Grisalez', '2024-03-31 23:47:25', '007', 'ACTIVO', '2MHOIFBB90');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cotizaciones`
--

CREATE TABLE `cotizaciones` (
  `num_cotizacion` varchar(20) NOT NULL,
  `cliente_cotizacion` varchar(10) NOT NULL,
  `documento_operador` varchar(10) NOT NULL,
  `nombre_operador` varchar(25) NOT NULL,
  `apellido_operador` varchar(25) NOT NULL,
  `fecha_inicio_cotizacion` date NOT NULL,
  `fecha_fin_cotizacion` date NOT NULL,
  `nombre_cliente_cotizacion` varchar(50) DEFAULT NULL,
  `estado` varchar(8) NOT NULL,
  `direcion_cliente` varchar(90) DEFAULT NULL,
  `correo_cliente` varchar(60) DEFAULT NULL,
  `cuidad_cliente` varchar(40) DEFAULT NULL,
  `contacto_cliente` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cotizaciones`
--

INSERT INTO `cotizaciones` (`num_cotizacion`, `cliente_cotizacion`, `documento_operador`, `nombre_operador`, `apellido_operador`, `fecha_inicio_cotizacion`, `fecha_fin_cotizacion`, `nombre_cliente_cotizacion`, `estado`, `direcion_cliente`, `correo_cliente`, `cuidad_cliente`, `contacto_cliente`) VALUES
('0873798', '26262626', '16385007', 'Hernan', 'Corrales Grisalez', '2024-03-16', '2024-03-22', 'NICOL', 'ACTIVO', 'CRA56#5455', 'DAHYA@GMAILXOM', 'BIHA', 'DAHYA@GMAILXOM'),
('1357983', '26262626', '16385007', 'Hernan', 'Corrales Grisalez', '2024-03-14', '2024-03-21', 'NICOL', 'ACTIVO', 'CRA56#5455', 'DAHYA@GMAILXOM', 'BIHA', 'DAHYA@GMAILXOM'),
('3034922', '1213145566', '1089000896', 'Edixon', 'Payan Hurtado', '2024-03-11', '2024-03-29', 'Nicol Maria ', 'ACTIVO', 'Tulua Centro', 'nicoafpos@gmail.com', 'Tulua ', 'nicoafpos@gmail.com'),
('5868983', '1616161616', '1089000896', 'Edixon', 'Payan Hurtado', '2024-03-11', '2024-03-29', 'Luis esteban', 'ACTIVO', 'cra1nb#aurescity', 'cliente1@gmail.com', 'buguita', 'cliente1@gmail.com'),
('7087853', '1213145566', '16385007', 'Hernan', 'Corrales Grisalez', '2024-04-01', '2024-04-06', 'Nicol Maria ', 'ACTIVO', 'Tulua Centro', 'nicoafpos@gmail.com', 'Tulua ', '3155127771'),
('7773072', '1213145566', '16385007', 'Hernan', 'Corrales Grisalez', '2024-03-14', '2024-03-21', 'Nicol Maria ', 'ACTIVO', 'Tulua Centro', 'nicoafpos@gmail.com', 'Tulua ', 'nicoafpos@gmail.com'),
('8528706', '33750742', '16385007', 'Hernan', 'Corrales Grisalez', '2024-03-16', '2024-03-22', 'kelly', 'ACTIVO', 'diagonal 13 # 11-22', 'kelly@gmail.com', 'Bogota', 'kelly@gmail.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detallecomprasproveedores`
--

CREATE TABLE `detallecomprasproveedores` (
  `id_detalle_compra` int(6) NOT NULL,
  `detallenum_compra` int(6) NOT NULL,
  `producto_compra` varchar(50) DEFAULT NULL,
  `cantidad_producto_compra` int(6) NOT NULL,
  `valorunidad_prodcompra` float NOT NULL,
  `valortotal_cantidadcomp` float NOT NULL,
  `totalpagar_compra` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `detallecomprasproveedores`
--

INSERT INTO `detallecomprasproveedores` (`id_detalle_compra`, `detallenum_compra`, `producto_compra`, `cantidad_producto_compra`, `valorunidad_prodcompra`, `valortotal_cantidadcomp`, `totalpagar_compra`) VALUES
(57, 63, 'Manija Ford Fiesta', 20, 10, 11, 200),
(58, 64, 'Motor elevavidrios original Kia', 11, 2000, 15000, 22000),
(59, 65, 'Tornillo exagonal alen', 20, 500, 10000, 0),
(60, 66, 'Manija INT LDD Hiunday 23', 22, 3000, 60000, 66000),
(61, 66, 'Manija INT LDD Hiunday 23', 22, 3000, 50000, 66000),
(62, 67, 'Motor elevavidrios original Kia', 20, 4000, 80000, 0),
(63, 68, 'Manija interna Chrevrolet LDD', 20, 2000, 20000, 40000),
(64, 68, 'Manija interna Chrevrolet LDD', 20, 2000, 3000, 40000);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detallecotizaciones`
--

CREATE TABLE `detallecotizaciones` (
  `id_detalle_cotizacion` int(6) NOT NULL,
  `num_cotizacion` varchar(20) NOT NULL,
  `producto_cotizacion` varchar(6) DEFAULT NULL,
  `nombre_producto` varchar(90) NOT NULL,
  `cantidad_productos_cotizacion` int(3) NOT NULL,
  `valorunidad_prodcotizacion` float NOT NULL,
  `valortotal_cantidaproductos_cotizacion` float NOT NULL,
  `totalpagar_cotizacion` float NOT NULL,
  `detalle_estado` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `detallecotizaciones`
--

INSERT INTO `detallecotizaciones` (`id_detalle_cotizacion`, `num_cotizacion`, `producto_cotizacion`, `nombre_producto`, `cantidad_productos_cotizacion`, `valorunidad_prodcotizacion`, `valortotal_cantidaproductos_cotizacion`, `totalpagar_cotizacion`, `detalle_estado`) VALUES
(65, '3034922', '474747', 'manija', 1, 5200, 5200, 5200, 'ACTIVO'),
(66, '3034922', '632737', 'motor limpia parabrisas kia', 1, 18000, 18000, 18000, 'ACTIVO'),
(67, '5868983', '123233', 'probando', 1, 2500, 2500, 2500, 'ACTIVO'),
(68, '5868983', '632737', 'motor limpia parabrisas kia', 1, 18000, 18000, 18000, 'ACTIVO'),
(69, '5868983', '474747', 'manija', 1, 5200, 5200, 5200, 'ACTIVO'),
(70, '1357983', '123233', 'motor limpia parabrisas para chevrolet', 1, 20000, 20000, 20000, 'ACTIVO'),
(71, '7773072', '123233', 'motor limpia parabrisas para chevrolet', 1, 20000, 20000, 20000, 'ACTIVO'),
(72, '0873798', '474747', 'manija', 1, 5200, 5200, 5200, 'ACTIVO'),
(73, '8528706', '123233', 'probando', 1, 2500, 2500, 2500, 'ACTIVO'),
(74, '7087853', '123233', 'parabrisas kia', 1, 30000, 30000, 30000, 'ACTIVO'),
(75, '7087853', '123233', 'motor limpia parabrisas para chevrolet', 1, 20000, 20000, 20000, 'ACTIVO');

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
(32, 36, 'motor limpia parabrisas kia - 100,   parabrisas kia - 21', 101, 0, 2430000, 0, 0, 0, 0, 2430000),
(33, 37, 'chapa derecha trasera chery y chevrolet - 90', 90, 0, 4950000, 0, 0, 0, 0, 4950000),
(34, 38, 'Chapa de seguridad Sandero - 1,   Empaque puerta delanteras - 38,   motor limpia parabrisas para chevrolet - 5', 44, 0, 251000, 0, 0, 0, 0, 251000),
(35, 39, 'motor limpia parabrisas para chevrolet - 1,   Empaque puerta delanteras - 2,   parabrisas kia - 6,   probando - 15', 24, 0, 246500, 0, 0, 0, 0, 246500),
(36, 40, 'parabrisas GT Ford - 2,   Empaque puerta delanteras - 1,   parabrisas kia - 30,   motor limpia parabrisas para chevrolet - 2,   parabrisas GMC - 12', 47, 0, 1116500, 0, 0, 0, 0, 1116500),
(37, 41, 'motor limpia parabrisas kia - 100', 100, 0, 1800000, 0, 0, 0, 0, 1800000),
(38, 42, 'motor limpia parabrisas kia - 30', 30, 0, 540000, 0, 0, 0, 0, 540000),
(39, 43, 'manija - 1,   motor limpia parabrisas kia - 31,   chapas puertas traseras chery q - 23', 55, 0, 1713200, 0, 0, 0, 0, 1713200),
(40, 44, 'manija - 40,   motor limpia parabrisas kia - 47', 87, 0, 1054000, 0, 0, 0, 0, 1054000),
(41, 45, 'Empaque puerta delanteras - 42', 42, 0, 189000, 0, 0, 0, 0, 189000),
(42, 46, 'parabrisas kia - 43', 43, 0, 1290000, 0, 0, 0, 0, 1290000),
(43, 47, 'manija - 21,   motor limpia parabrisas kia - 30,   parabrisas kia - 34', 85, 0, 1669200, 0, 0, 0, 0, 1669200),
(44, 48, 'manija - 2,   motor limpia parabrisas kia - 4,   probando - 2,   parabrisas kia - 3,   chapas puertas traseras chery q - 1,   manija hiunday - 1', 13, 0, 242400, 0, 0, 0, 0, 242400),
(45, 49, 'motor limpia parabrisas kia - 1,   motor limpia parabrisas para chevrolet - 1,   motor limpia parabrisas para chevrolet - 1', 3, 0, 39000, 0, 0, 0, 0, 39000),
(46, 50, 'probando - 1', 1, 0, 2500, 0, 0, 0, 0, 2500),
(47, 51, 'motor limpia parabrisas kia - 28,   parabrisas kia - 1,   Empaque puerta delanteras - 1,   manija - 2', 32, 0, 548900, 0, 0, 0, 0, 548900),
(48, 52, 'probando - 32,   parabrisas GT Ford - 1,   parabrisas kia - 5', 38, 0, 245000, 0, 0, 0, 0, 245000),
(49, 53, 'probando - 24,   motor limpia parabrisas kia - 3', 27, 0, 114000, 0, 0, 0, 0, 114000),
(50, 54, 'manija - 17', 17, 0, 88400, 0, 0, 0, 0, 88400),
(51, 55, 'manija hiunday - 96', 96, 0, 1440000, 0, 0, 0, 0, 1440000),
(52, 56, 'parabrisas GMC - 31,   parabrisas GT Ford - 41,   parabrisas kia - 20', 92, 0, 1649000, 0, 0, 0, 0, 1649000),
(53, 57, 'deposito de tres - 1', 1, 0, 140000, 0, 0, 0, 0, 140000);

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
('1086358507', 'dennis', 'echeverri', '2023-11-17', '3006888865', 'dennisecheverri46@gmail.com', 'Cajuijio', 'pasto', 'a459867974f1bcc8fc7f1ef07d6373355cfeba01241778822f09127726073b5d98daeb5fc174861fbd2738de2c535d78abe92249e04abb6e7a3bb7b75f98e3b5', ' administrado', NULL, '2023-11-14 18:30:07', '', '', '', 'ACTIVO'),
('1089000896', 'Edixon De Nataly', 'Payan Hurtado', '2003-03-02', '3145241834', 'edixonpayan8@gmail.com', 'Calle 6 # 6-89', 'buga', 'ba3253876aed6bc22d4a6ff53d8406c6ad864195ed144ab5c87621b6c233b548baeae6956df346ec8c17f5ea10f35ee3cbc514797ed7ddd3145464e2a0bab413', 'administrador', NULL, '2024-03-01 18:08:06', '', '', '', 'ACTIVO'),
('1111035245', 'Herney', 'Grisalez', '2024-02-15', '3041144554', 'herney@gamil.com', 'Calle 21 #4-09', 'Buga', '3627909a29c31381a071ec27f7c9ca97726182aed29a7ddd2e54353322cfb30abb9e3a6df2ac2c20fe23436311d678564d0c8d305930575f60e2d3d048184d79', 'vendedor', NULL, '2024-02-02 20:22:10', '', '', '', 'INACTIVO'),
('1112388921', 'Nicol', 'Motoa', '0000-00-00', NULL, 'dahyanna.me@gmail.com', '', '', '3b1c2ae69435c86e2982ab43b8e580b4041c67ff7c1717a0f508a958ce0dba52320c2373b77212cbdd5c8302b4498121fc6fd28da611382b94684e2d9085b591', ' administrador', NULL, '0000-00-00 00:00:00', '', '', '', 'INACTIVO'),
('16161616', 'Andres', 'Velasco', '1970-12-19', '3003003003', 'afvelasco@gmail.com', 'Calle 6 # 6-6', 'Buga', 'Abcde+12345', ' administrador', NULL, '2023-10-26 19:39:44', '', '', '', 'ACTIVO'),
('16385007', 'Hernan', 'Corrales Grisalez', '1981-09-04', '3122175402', 'edcorgriz@hotmail.com', 'Carrera 8 #13-11', 'Buga', '3627909a29c31381a071ec27f7c9ca97726182aed29a7ddd2e54353322cfb30abb9e3a6df2ac2c20fe23436311d678564d0c8d305930575f60e2d3d048184d79', 'administrador', NULL, '2023-12-26 17:23:47', '', '', '', 'ACTIVO'),
('193838362', 'Edixon', 'Payan', '2003-03-28', '3162532732', 'edixonpayan5@gmail.com', 'barrio tamarindo calle 1 #24-65', 'buga', 'ecc768c8f4b939f0bd5d4ba36a07723d5cf4064a3c9124496a255cc5013de04b1370d16bb9f1e8bab7daec84a447ca95e5e4d9a002aa74bf36399c41209d9c5c', 'administrador', NULL, '2023-10-09 09:13:44', '', '', '', 'ACTIVO'),
('312244556', 'Nicol de De', 'Sebas2', '2004-09-28', '316553344', 'nicolmotoa.28@gmail.com', 'Carrera 33 # 66-66', '', '3627909a29c31381a071ec27f7c9ca97726182aed29a7ddd2e54353322cfb30abb9e3a6df2ac2c20fe23436311d678564d0c8d305930575f60e2d3d048184d79', '', NULL, '2023-12-26 19:25:03', '', '', '', 'ACTIVO'),
('94447540', 'Eduar', 'Corrales', '0000-00-00', 'None', 'edcorgris@gmail.com', 'Carrera 50 #4-09', 'Sonso', '394919744eb6de1aee9a0fa0fa4330f9c13db999379f93b5e4ae7dd5e715972d90b3920213c52a0f24acb8675321a865aef38146cb2f2ce0e30952f10321ea61', ' administrador', NULL, '0000-00-00 00:00:00', '', '', '', 'ACTIVO');

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

--
-- Volcado de datos para la tabla `historial_credito`
--

INSERT INTO `historial_credito` (`contador`, `contador_ventacredito`, `abono`, `operador`, `fecha_abono`) VALUES
(1, 12, 700, 193838362, '2024-03-05 20:01:11'),
(2, 12, 20000, 193838362, '2024-03-05 20:01:37');

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
(474747, 'manija original renault2', 'mani renault 2000', 'listados', 2, 'Manijas', '1133445560', 'Posad FVELA', 'manija', 25, 5200, 15, 'fjoierfjajflas', 10, 'Bodega', 7, '2023-10-18 20:22:17', '94447540', 'Eduar', 'Corrales', 'ACTIVO'),
(6327372, 'mot lim kia', 'mot lim kia rio', 'mot lim kia space', 3, 'motor llimpia parabrisas kia', '1133445566', 'oto', 'motor limpia parabrisas kia', 12000, 18000, 13, 'motor limpia parabrisas marca kia todos los modelos del 2022-2024', 10, 'Bodega', 66, '2023-10-03 12:28:50', '94447540', 'Eduar', 'Corrales', 'ACTIVO'),
(12323334, 'udhs', '', '', 1, '', '1133445560', 'oto', 'probando', 2000, 2500, 212, 'algo nuevo', 3, '1', 3, '2023-10-03 12:19:48', '94447540', 'Eduar', 'Corrales', 'ACTIVO'),
(12323335, 'parabrisa kia sportage', 'parabrisa kia rio', 'parabrisa kia ', 1, 'parabrisas', '02020202', 'oto', 'parabrisas kia', 20000, 30000, 351, 'Prabrisas Kia sportage, rio, soul modelo 2016-2024', 4, 'Bodega', 8, '2024-01-22 16:28:15', '16385007', 'Hernan', 'Corrales', 'ACTIVO'),
(12323336, 'empaque puerta delantera ford', 'empaque puerta dodge', 'empaque puerta chevrolet', 4, 'empaques', '1717171717', 'Prueba1', 'Empaque puerta delanteras', 35000, 4500, 202, 'Empaque para puerta doble canal original ford', 30, 'Bodega', 5, '2024-01-24 20:37:48', '16385007', 'Hernan', 'Corrales', 'ACTIVO'),
(12323338, '94477540', '23f', '24r', 1, 'parabrisas', '02020202', 'oto', 'parabrisas GMC', 12000, 14000, 315, 'parabrias GMC modelo 2000-2023', 2, 'Bodega', 1, '2024-02-01 19:38:35', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
(12323339, 'parab1', 'parab2', 'parab3', 1, 'parabrisas', '1133445566', 'AFV ECHEVERI', 'parabrisas GT Ford', 120000, 15000, 155, 'parabrisas para Ford Gt', 2, 'Bodega', 2, '2024-02-02 16:09:01', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
(12323340, '1PCBA\'U01\'S07ZAR', '94477540', 'Q1', 2, 'Manijas', '1717171717', 'Prueba1', 'manija hiunday', 10000, 15000, 301, 'manija hiunday original', 4, 'Almacen', 3, '2024-02-02 19:15:30', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
(12323341, '97895856771669786073133333', '9786073133333', '2PD', 3, 'chapas', '11338787', 'Posad FVELASCO', 'chapas puertas traseras chery q', 30000, 50000, 576, 'chapa chery q puertas traseras lado derecho', 3, 'Bodega', 34, '2024-02-02 19:20:35', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
(12323342, 'chapa rb24', 'chapa chery qrb', 'chapa chevrolet rb', 3, 'chapas', '02020202', 'oto', 'chapa derecha trasera chery y chevrolet', 35000, 55000, 530, 'chapa puerta trasera derecha para chery chevrolet modelo 2020-2024', 10, 'Bodega', 45, '2024-02-02 19:24:45', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
(12323343, '2PDCN', '1PCBA\'U01\'S07ZAR', '94477540eh', 1, 'parabrisas', '02020202', 'oto', 'Empaque puerta doble canal Renault', 20000, 33000, 290, 'Empaque para puerta doble canal original ford', 2, 'Bodega', 2, '2024-02-02 20:03:17', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
(12323344, 'motor limpia parabrisas chevrolet', 'motor limpia parabrisas chery', 'motor gm', 7, 'motor llimpia parabrisas', '1717171717', 'Prueba1', 'motor limpia parabrisas para chevrolet', 150000, 20000, 569, 'motor limpia parabrisas para chevrolet, chery modelos 2010-2024', 4, 'Bodega', 5, '2024-02-05 08:29:44', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
(12323345, '864904050363710', '31802-k2qu00633', '77024411', 3, 'chapas', '1133445560', 'Posad FVELA', 'Chapa de seguridad Sandero', 5000000, 100000, 179, 'jlksjf lkasj lk alskdjkasljl', 2, 'Bodega', 0, '2024-02-05 20:28:49', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
(12323346, 'motor limpia parabrisas chevrolet', 'Motor chevy 111', 'motor chevrolet', 7, 'motor llimpia parabrisas', '1133445566', 'AFV ECHEVERI', 'motor limpia parabrisas para chevrolet', 100, 7000, 297, 'motor limpia parabrisas para chevrolet, chery modelos 2010-2024', 40, 'Bodega', 4, '2024-02-08 16:00:32', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
(12323347, ' motor limpia parabrisas chevrolet', 'motor limpia parabrisas chery', 'motor gm', 7, 'motor llimpia parabrisas', '2323232323', 'DAHYANNA', 'motor limpia parabrisas para chevrolet', 100, 14000, 294, 'motor limpia parabrisas para chevrolet, chery modelos 2010-2024', 10, 'Bodega', 44, '2024-02-08 16:49:30', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
(12323348, 'MNCH2024', '', '', 9, 'Miona Chevrolet', '1133445566', 'Juan Fernando Echeverry', 'Miona CH Aveo', 120000, 150000, 20, 'Miona Chevrolet Aveo 2020-2024', 5, 'Bodega', 4, '2024-03-27 11:43:10', '16385007', 'Hernan', 'Corrales Grisalez', 'INACTIVO'),
(12323349, 'Motor Limpia Parabrisas Chevrolet Aveo', '', '', 7, 'motor llimpia parabrisas', '1133445566', 'Juan Fernando Echeverry', 'motor limpia parabrisas para chevrolet ', 12000, 15000, 34, 'Motor limpia parabrisas Chevrolet Aveo modelo 2000', 5, 'Bodega', 7, '2024-03-27 12:59:16', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
(12323350, 'Radio11', '', '', 2, 'Manijas', '1133445572', 'AFNICOL', 'Radio Better', 15000, 15001, 51, 'Radio vehicular marca Better', 5, 'Bodega', 5, '2024-03-28 11:09:47', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
(12323351, 'man1', '', '', 2, 'Manijas', '2323232323', 'DAHYANNA', 'Manija plastica Kia', 1200, 1300, 50, 'Manija Kia plastica modelos Sportage Cerato 2000-2024', 7, 'Bodega', 9, '2024-03-28 11:11:46', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
(12323352, 'cha2', '', '', 3, 'chapas', '1133445566', 'Juan Fernando Echeverry', 'chapa dos', 120000, 130000, 30, 'chapados de dos', -5, 'Bodega', 5, '2024-03-28 11:15:46', '16385007', 'Hernan', 'Corrales Grisalez', 'INACTIVO'),
(12323353, 'deposito', '', '', 1, 'parabrisas', '1133445569', 'Posada Juan FVELA', 'deposito de tres', 130000, 140000, 5, 'depsoito de dos y tres', 5, 'Bodega', 8, '2024-03-28 11:19:37', '16385007', 'Hernan', 'Corrales Grisalez', 'INACTIVO'),
(12323354, 'tronillof2', '', '', 2, 'Manijas', '1133445572', 'AFNICOL', 'tornilo f2 y f3', 1.5, 1.501, 50, 'tornilo que aprietta todo', 5, 'Bodega', 5, '2024-03-28 11:56:44', '16385007', 'Hernan', 'Corrales Grisalez', 'INACTIVO'),
(12323355, 'tor', '', '', 3, 'chapas', '2323232323', 'DAHYANNA', 'tortugados', 14000, 15000, 55, 'tortugas para dos', 5, 'Bodega', 6, '2024-03-28 12:28:43', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
(12323356, 'TB13a', '', '', 5, 'eleva vidrio', '1133445572', 'AFNICOL', 'Tubo de 13\"', 35000, 35002, 400, 'tubo de 13\" galvanizado', -10, 'Bodega', 7, '2024-03-28 12:30:44', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
(12323357, 'rtf23', '', '', 1, 'parabrisas', '1133445570', 'Posad FVELASCO', 'retfefefefe', 12000, 13000, 44, 'retefe y mas fe', 5, 'Almacen', 5, '2024-03-28 12:40:08', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
(12323358, 'tr23', '', '', 1, 'parabrisas', '1133445566', 'Juan Fernando Echeverry', 'tr23-2024', 155000, 155001, 55, 'tre23-2024 y mas', -6, 'Bodega', 8, '2024-03-28 12:43:43', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
(12323359, 'toro2', '', '', 1, 'parabrisas', '1133445572', 'AFNICOL', 'toro2 en 1', 1000, 1200, 20, 'toro dos en uno', 4, 'Bodega', 8, '2024-03-28 12:51:01', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
(12323360, 'torre1', '', '', 1, 'parabrisas', '1133445572', 'AFNICOL', 'torre1 parabrisa', 350000, 420000, 45, 'parabrisas torre 1', 7, 'Bodega', 4, '2024-03-28 15:21:22', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO');

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
('1133445560', 'Posad ', '3144455678', 'edccor@hotmail.om', 'Calle 6sur #13b40', 'Santiago de Ca', '2023-09-27 16:25:22', '16385007', 'Hernan', 'Corrales Grisalez', 'INACTIVO'),
('1133445566', 'Juan Fernando Echeverry', '3144455678', 'edccor@hotmail.om', 'Calle 6sur #13b40', 'Cali', '2023-09-27 16:21:41', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
('1133445569', 'Noelia Rivas ', '3133355678', 'edccor@hotmail.om', 'Calle 6sur #13b40', 'Cali', '2023-09-27 16:24:34', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
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
('90056458', 'Vidrios del Valle', '3105674546', 'vidriosvalle@gmail.com', 'Carrera 5 # 16-88', 'Cali', '2024-03-31 16:40:05', '16385007', 'Hernan', 'Corrales Grisalez', 'ACTIVO'),
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
(2, 'edcorgris@gmail.com', '2023-12-23 20:36:15', '2023-12-23 20:39:15', '49nLo83UBdzPZcV3ofZ9H9OO785CYuqW', '94447540', 'si'),
(4, 'edixonpayan5@gmail.com', '2024-02-10 17:37:37', '2024-02-10 17:40:37', 'fOTB3Tzv5Fzida9RjjrdgJt8DfGMqpRC', '193838362', 'si'),
(5, 'edixonpayan5@gmail.com', '2024-03-01 18:19:51', '2024-03-01 18:22:51', 'fYnYCBvkDTVyJBAdbN5Qnw9fxHZzTvEl', '193838362', 'si'),
(6, 'dahyanna.me@gmail.com', '2024-03-04 17:41:32', '2024-03-04 17:44:32', 'ABYMKccbcpJ2iGDkMnsGRxslkUGipK7I', '1112388921', 'no'),
(7, 'edixonpayan5@gmail.com', '2024-03-08 12:08:43', '2024-03-08 12:11:43', 'ipWfqC8AweoJEIPsGbdcFxZbfyn0WT1n', '193838362', 'si'),
(8, 'edixonpayan5@gmail.com', '2024-03-08 12:41:32', '2024-03-08 12:44:32', 'PyOUGSgXoP9Wrn7IkDwzd5jak9Ym4XnY', '193838362', 'si');

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
  `email_empleado` varchar(50) NOT NULL,
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
(24, '1111035245', 'Herney', 'herney@g', 'y18puDuaGuuunGYhDvivSqx1H9V9TFdE', 'no confirmado', '2024-02-02 20:22:10'),
(27, '1089000896', 'Edixon', 'edixonpayan8@gmail.com', 'BPvcHW1ZGG1acs2J2YbEvOCKllbpVtSC', 'confirmado', '2024-03-01 18:08:06');

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
(36, '33750742', 0, '193838362', 'Edixon', 'Payan', '2024-02-26 14:46:37', 'efectivo', NULL, 'WSFPL6uhyx3HGCqfgJE4', NULL),
(37, '33750742', 0, '193838362', 'Edixon', 'Payan', '2024-03-01 14:47:48', 'efectivo', NULL, 'yhgW8p7rGXVxicYDlsQZ', NULL),
(38, '33750742', 0, '193838362', 'Edixon', 'Payan', '2024-02-26 14:48:14', 'efectivo', NULL, 'KQvjNLmebMYfk13TIUia', NULL),
(39, '33750742', 0, '193838362', 'Edixon', 'Payan', '2024-02-29 14:48:45', 'Tarjeta cred', NULL, 'GxpwaYDvhIZ5U7nK0eXS', NULL),
(40, '33750742', 0, '193838362', 'Edixon', 'Payan', '2024-02-28 14:49:34', 'Daviplata', NULL, 'R8pA1ZDdojKUvS6MuPit', NULL),
(41, '33750742', 0, '193838362', 'Edixon', 'Payan', '2024-02-27 18:19:01', 'Bancolombia', NULL, 'dVjh2B4W5qEsOy9kCPFf', NULL),
(42, '33750742', 0, '193838362', 'Edixon', 'Payan', '2024-02-27 19:11:34', 'efectivo', NULL, 'zTaI84pCU15xPMKOGVBD', NULL),
(43, '33750742', 0, '193838362', 'Edixon', 'Payan', '2024-03-05 19:47:54', 'Tarjeta debi', NULL, 'LEXq4lZ71aMny8eW59Jd', NULL),
(44, '33750742', 0, '193838362', 'Edixon', 'Payan', '2024-03-05 23:59:38', 'efectivo', NULL, 'Swlyh8Z5UIHR0pXuBs6g', NULL),
(45, '33750742', 0, '193838362', 'Edixon', 'Payan', '2024-03-06 00:01:48', 'efectivo', NULL, 'o67bheYdkqpLDv3wJVE0', NULL),
(46, '33750742', 0, '193838362', 'Edixon', 'Payan', '2024-03-06 00:23:42', 'efectivo', NULL, 'nbuv7Ct5gHr8NBIh1lAF', NULL),
(47, '33750742', 0, '193838362', 'Edixon', 'Payan', '2024-03-12 02:31:51', 'efectivo', NULL, '0zR6yq1rWiJxOVkLMaDT', NULL),
(48, '33750742', 0, '193838362', 'Edixon', 'Payan', '2024-03-12 02:53:55', 'efectivo', NULL, 'ZpYeqy7mFHdtn9TVrbL6', NULL),
(49, '33750742', 0, '193838362', 'Edixon', 'Payan', '2024-03-11 02:58:13', 'efectivo', NULL, '3MdBHIAcCrU2ObJqThP8', NULL),
(50, '33750742', 0, '193838362', 'Edixon', 'Payan', '2024-03-11 02:58:40', 'efectivo', NULL, '8iHyCNVJdS7rpgxZB9ID', NULL),
(51, '33750742', 0, '193838362', 'Edixon', 'Payan', '2024-03-12 15:35:27', 'efectivo', NULL, 'ts5Elp9VKgTeHU13F4aO', NULL),
(52, '33750742', 0, '193838362', 'Edixon', 'Payan', '2024-03-11 15:37:00', 'efectivo', NULL, 'yE2CDrxoSWcjtz506l9e', NULL),
(53, '33750742', 0, '193838362', 'Edixon', 'Payan', '2024-03-12 17:18:58', 'efectivo', NULL, 'LZNnsJmD5uCFQVIEHhto', NULL),
(54, '33750742', 0, '193838362', 'Edixon', 'Payan', '2024-03-11 17:19:52', 'efectivo', NULL, 'RjuC6NvdhKMS3g2Q5lfm', NULL),
(55, '33750742', 0, '193838362', 'Edixon', 'Payan', '2024-03-11 17:21:12', 'efectivo', NULL, 'czWYKhNa97o0PGl4Vu5A', NULL),
(56, '33750742', 0, '193838362', 'Edixon', 'Payan', '2024-03-11 17:37:01', 'efectivo', NULL, 'OIXdEu93y4s8lQwKfkPz', NULL),
(57, '1213145566', 0, '16385007', 'Hernan', 'Corrales Grisalez', '2024-03-28 11:43:46', 'efectivo', NULL, '9djh753GMbasPUuI0Tn1', NULL);

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
(1, '1213145566', 'probando, tornillos, probando', 700, 700, 1086358507, '2023-11-14 21:21:09', 'ACTIVO'),
(2, '1213145566', 'manija - 3', 15600, 15600, 193838362, '2024-02-22 22:04:57', 'ACTIVO'),
(3, '1213145566', 'manija - 1,   motor limpia parabrisas kia - 1,   probando - 1', 25700, 25700, 193838362, '2024-02-22 22:57:32', 'ACTIVO'),
(4, '1213145566', 'Empaque puerta delanteras - 1,   probando - 1,   motor limpia parabris', 25000, 25000, 193838362, '2024-02-22 22:58:01', 'ACTIVO'),
(5, '1213145566', 'parabrisas kia - 1,   Empaque puerta delanteras - 1,   parabrisas GMC ', 71700, 71700, 193838362, '2024-02-22 22:58:23', 'ACTIVO'),
(6, '1213145566', 'probando - 1,   parabrisas kia - 1', 32500, 32500, 193838362, '2024-02-23 00:21:24', 'ACTIVO'),
(7, '1213145566', 'probando - 1,   parabrisas kia - 1', 32500, 32500, 193838362, '2024-02-23 00:23:14', 'ACTIVO'),
(8, '1213145566', 'manija - 1,   parabrisas kia - 1', 35200, 35200, 193838362, '2024-02-23 00:43:34', 'ACTIVO'),
(9, '1213145566', 'probando - 1', 2500, 2500, 193838362, '2024-02-23 00:45:27', 'ACTIVO'),
(10, '33750742', 'manija - 1,   motor limpia parabrisas kia - 1,   probando - 1,   parab', 55700, 55700, 193838362, '2024-03-05 19:16:53', 'ACTIVO'),
(11, '33750742', 'manija - 1,   motor limpia parabrisas kia - 1,   parabrisas kia - 1', 53200, 53200, 193838362, '2024-03-05 19:32:07', 'ACTIVO'),
(12, '33750742', 'manija - 1,   probando - 1,   parabrisas kia - 1', 37700, 0, 193838362, '2024-03-05 19:46:00', 'ACTIVO'),
(13, '44337765', 'manija - 1,   motor limpia parabrisas kia - 1', 23200, 23200, 193838362, '2024-03-06 02:10:41', 'ACTIVO');

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
  MODIFY `contador` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=147;

--
-- AUTO_INCREMENT de la tabla `categorias`
--
ALTER TABLE `categorias`
  MODIFY `id_categoria` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `comprasproveedores`
--
ALTER TABLE `comprasproveedores`
  MODIFY `num_compra` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;

--
-- AUTO_INCREMENT de la tabla `detallecomprasproveedores`
--
ALTER TABLE `detallecomprasproveedores`
  MODIFY `id_detalle_compra` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=65;

--
-- AUTO_INCREMENT de la tabla `detallecotizaciones`
--
ALTER TABLE `detallecotizaciones`
  MODIFY `id_detalle_cotizacion` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=76;

--
-- AUTO_INCREMENT de la tabla `detalledevoluciones`
--
ALTER TABLE `detalledevoluciones`
  MODIFY `id_detalle_devolucion` int(6) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `detalleventas`
--
ALTER TABLE `detalleventas`
  MODIFY `id_detalle_factura` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=54;

--
-- AUTO_INCREMENT de la tabla `devoluciones`
--
ALTER TABLE `devoluciones`
  MODIFY `id_devolucion` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `historial_credito`
--
ALTER TABLE `historial_credito`
  MODIFY `contador` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id_producto` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12323361;

--
-- AUTO_INCREMENT de la tabla `recuperarcontrasena`
--
ALTER TABLE `recuperarcontrasena`
  MODIFY `id_solicitud` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `servicios`
--
ALTER TABLE `servicios`
  MODIFY `id_servicio` int(6) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tokens`
--
ALTER TABLE `tokens`
  MODIFY `id_token` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT de la tabla `ubicacion`
--
ALTER TABLE `ubicacion`
  MODIFY `num_estante` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `ventas`
--
ALTER TABLE `ventas`
  MODIFY `num_factura` int(6) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=58;

--
-- AUTO_INCREMENT de la tabla `ventas_credito`
--
ALTER TABLE `ventas_credito`
  MODIFY `contador` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

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
