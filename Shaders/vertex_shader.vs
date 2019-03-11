#version 330

layout (location = 0) in vec3 position;
layout (location = 1) in vec3 vertNormal;

uniform mat4 proj;
uniform mat4 view;
uniform mat4 model;
uniform mat4 light;

out vec3 fragNormal;
out vec3 fragPos;

void main()
{
    gl_Position = proj * view * model * vec4(position, 1.0);
    fragPos = vec3(model * vec4(position, 1.0));
    fragNormal = vertNormal;
}