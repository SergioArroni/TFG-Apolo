// Importar los módulos necesarios
const express = require('express');
const bodyParser = require('body-parser');
const session = require('express-session');
const bcrypt = require('bcrypt');

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

app.post('/registro', async (req, res) => {
    const { nombre, email, password } = req.body;
    // Validar los datos del formulario
    if (!nombre || !email || !password) {
        return res.status(400).send('Falta información en el formulario');
    }
    // Verificar que el email no esté en uso
    const usuarioExistente = await buscarUsuarioPorEmail(email);
    if (usuarioExistente) {
        return res.status(409).send('El email ya está en uso');
    }
    // Crear el nuevo usuario
    const passwordHash = await bcrypt.hash(password, 10);
    const nuevoUsuario = {
        nombre,
        email,
        password: passwordHash
    };
    await guardarUsuario(nuevoUsuario);
    // Iniciar la sesión del usuario
    req.session.usuario = nuevoUsuario;
    res.redirect('/catalogo');
});

app.get('/login', (req, res) => {
    res.send('Formulario de inicio de sesión');
});

app.post('/login', async (req, res) => {
    const { email, password } = req.body;
    // Validar los datos del formulario
    if (!email || !password) {
        return res.status(400).send('Falta información en el formulario');
    }
    // Verificar las credenciales del usuario
    const usuario = await buscarUsuarioPorEmail(email);
    if (!usuario) {
        return res.status(401).send('Credenciales inválidas');
    }
    const passwordMatch = await bcrypt.compare(password, usuario.password);
    if (!passwordMatch) {
        return res.status(401).send('Credenciales inválidas');
    }
    // Iniciar la sesión del usuario
    req.session.usuario = usuario;
    res.redirect('/catalogo');
});

app.get('/catalogo', (req, res) => {
    // Verificar si el usuario está autenticado
    if (!req.session.usuario) {
        return res.redirect('/login');
    }
    res.send('Catálogo de plantas');
});

app.get('/compra', (req, res) => {
    // Verificar si el usuario está autenticado
    if (!req.session.usuario) {
        return res.redirect('/login');
    }
    res.send('Formulario de compra');
});

app.post('/compra', (req, res) => {
    // Código para procesar el formulario de compra
});

// Funciones auxiliares
async function buscarUsuarioPorEmail(email) {
    // Código para buscar un usuario en la base de datos por su email
}

async function guardarUsuario(usuario) {
    // C
