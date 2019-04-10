#version 330

in vec3 vertexColor;
out vec3 outColor;

void main()
{
    float ambientStrength = 0.9;
    vec3 lightColor = vec3(0.8, 0.8, 0.8);
    vec3  ambient = ambientStrength * lightColor;

    vec3 result = ambient * vertexColor;
    outColor = result;
}