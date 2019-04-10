#version 330

layout (location = 0) in vec3 position;
layout (location = 1) in vec3 aNormal;

out vec3 FragPos;
out vec3 Normal;

out vec3 vertexColor;
uniform vec3 myColor;

uniform mat4 proj;
uniform mat4 view;
uniform mat4 model;
uniform mat4 scale;
uniform mat4 rot_x;
uniform mat4 rot_y;

void main()
{
    vertexColor = myColor;
    gl_Position = proj * view * model * rot_y * rot_x * scale * vec4(position, 1.0);
    FragPos = vec3(model * vec4(position, 1.0));
    Normal = aNormal;
}