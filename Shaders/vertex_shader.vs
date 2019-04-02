#version 330

layout (location = 0) in vec3 position;

out vec4 vertexColor;
uniform vec3 myColor;

uniform mat4 proj;
uniform mat4 view;
uniform mat4 model;

uniform mat4 scale;

void main()
{
    vertexColor = vec4(myColor, 1.0);
    gl_Position = proj * view * model * scale * vec4(position, 1.0);
}