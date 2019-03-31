#version 330

layout (location = 0) in vec3 position;

uniform mat4 proj;
uniform mat4 view;
uniform mat4 model;

uniform mat4 scale;
uniform mat4 transf;

void main()
{
    gl_Position = transf * scale * proj * view * model * vec4(position, 1.0);
}