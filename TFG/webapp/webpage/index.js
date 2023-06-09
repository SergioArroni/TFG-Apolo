// Importar los módulos necesarios
const express = require('express');
const bodyParser = require('body-parser');
const session = require('express-session');

// Crear la aplicación
const app = express();

// Configurar el middleware
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(session({
    secret: 'supersecreto',
    resave: false,
    saveUninitialized: true
}));

// Definir las rutas
app.get('/', (req, res) => {
    res.send('Bienvenido a nuestra tienda de plantas');
});

app.get('/registro', (req, res) => {
    res.send('Formulario de registro');
});

app.post('/registro', (req, res) => {
    // Código para procesar el formulario de registro
});

app.get('/login', (req, res) => {
    res.send('Formulario de inicio de sesión');
});

app.post('/login', (req, res) => {
    // Código para procesar el formulario de inicio de sesión
});

app.get('/catalogo', (req, res) => {
    res.send('Catálogo de plantas');
});

app.get('/compra', (req, res) => {
    res.send('Formulario de compra');
});

app.post('/compra', (req, res) => {
    // Código para procesar el formulario de compra
});

// Iniciar el servidor
const port = 3000;
app.listen(port, () => {
    console.log(`Servidor iniciado en http://localhost:${port}`);
});
