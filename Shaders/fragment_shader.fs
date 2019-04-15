#version 330

in vec3 Normal;
in vec3 FragPos;

in vec3 vertexColor;
out vec3 outColor;

void main()
{
    float ambientStrength = 0.9;
    vec3 lightColor = vec3(0.8, 0.8, 0.8);
    vec3 ambient = ambientStrength * lightColor; // llum natural

    vec3 lightPos = vec3(3.0, 3.0, 3.0);
    vec3 lightDir = normalize(FragPos - lightPos);
    // vec3 norm = normalize(Normal);
    float diff = max(dot(Normal, lightDir), 0.0);
    vec3 diffuse = diff * lightColor;
    vec3 res2 = (ambient + diffuse) * vertexColor;

    // vec3 sunLightIntensity = vec3(0.9f, 0.9f, 0.9f);
    // vec3 sunLightDirection = normalize(vec3(-2.0, -2.0, 0.0));
    // vec3 result = ambient + sunLightIntensity * max(dot(Normal, sunLightDirection), 0.0);

    outColor = res2; //result * vertexColor;
}