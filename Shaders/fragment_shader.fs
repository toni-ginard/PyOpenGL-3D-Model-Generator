#version 330

in vec3 Normal;
uniform vec3 lightPos = vec3(1.2, 1.0, 2.0);
in vec3 FragPos;

in vec3 vertexColor;
out vec3 outColor;

void main()
{
    float ambientStrength = 0.9; // intensitat llum
    vec3 lightColor = vec3(1.0, 0.4, 0.0); // color llum
    vec3  ambient = ambientStrength * lightColor; // llum natural

    vec3 norm = normalize(Normal);
    vec3 lightDir = normalize(lightPos - FragPos);
    float diff = max(dot(norm, lightDir), 0.0);
    vec3 diffuse = diff * lightColor;

    vec3 result = (ambient + diffuse) * vertexColor;
    // vec3 result = ambient * vertexColor;
    outColor = result;
}