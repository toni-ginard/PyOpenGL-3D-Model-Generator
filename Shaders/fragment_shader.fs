#version 330

in vec3 Normal;
in vec3 FragPos;

in vec3 vertexColor;
out vec3 outColor;

void main()
{
    float ambientStrength = 0.9; // intensitat llum
    vec3 lightColor = vec3(0.8, 0.8, 0.8); // color llum
    vec3 ambient = ambientStrength * lightColor; // llum natural

    vec3 sunLightIntensity = vec3(0.9f, 0.9f, 0.9f);
    vec3 sunLightDirection = normalize(vec3(-2.0, -2.0, 0.0));

    vec3 result = ambient + sunLightIntensity * max(dot(Normal, sunLightDirection), 0.0);

    outColor = result * vertexColor;
}