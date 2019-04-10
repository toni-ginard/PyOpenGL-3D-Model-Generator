#version 330

in vec3 Normal;
in vec3 FragPos;
uniform vec3 lightPos;

in vec3 vertexColor;
out vec3 outColor;

void main()
{
    float ambientStrength = 0.9; // intensitat llum
    vec3 lightColor = vec3(0.8, 0.8, 0.8); // color llum
    vec3  ambient = ambientStrength * lightColor; // llum natural

    vec3 norm = normalize(Normal);
    vec3 lightDir = normalize(lightPos - FragPos);

    vec3 result = ambient * vertexColor;
    outColor = result;
}