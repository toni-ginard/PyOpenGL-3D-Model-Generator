from OpenGL.GL import *
import OpenGL.GL.shaders
import pyrr

class Shader:

    @staticmethod
    def vertex_shader():
        return """
                #version 330
                in layout (location = 0) vec3 position;
                in layout (location = 1) vec2 textureCoords;
                
                uniform mat4 proj;
                uniform mat4 view;
                uniform mat4 model;
                
                out vec2 newTexture;
                void main()
                {
                    gl_Position = proj * view * model * vec4(position, 1.0);
                    newTexture = textureCoords;
                }
                """

    @staticmethod
    def fragment_shader(r, g, b):
        return """
                #version 330
                out vec4 outColor;
                in vec2 newTexture;
                uniform sampler2D samplerTexture;
                void main()
                {
                    outColor = texture(samplerTexture, newTexture); 
                }
                """

    @staticmethod
    def compilar_shaders(vertex_shader, fragment_shader):
        # shader: l'utilitzam per renderitzar
        return OpenGL.GL.shaders.compileProgram(OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
                                                OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER))

    # mac
    @staticmethod
    def bind_vao():
        vao = glGenVertexArrays(1)  # mac
        glBindVertexArray(vao)      # mac

    # copiar a la memoria el buffer de la figura
    @staticmethod
    def bind_vbo(figura):
        vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)  # vincular 2 buffers
        glBufferData(GL_ARRAY_BUFFER, figura.nbytes, figura, GL_STATIC_DRAW)

    # copiar a la memoria el buffer dels indexs
    @staticmethod
    def bind_ebo(indexs_figura):
        ebo = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indexs_figura.nbytes, indexs_figura, GL_STATIC_DRAW)

    @staticmethod
    def get_atribut(shader, atribut):
        return glGetAttribLocation(shader, atribut)

    @staticmethod
    def vertex_attrib(offset):
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 12, ctypes.c_void_p(offset))
        glEnableVertexAttribArray(0)  # 1 vertex son 3 coordenades float = 12 bytes
        # 0 o atribut ("position")

    @staticmethod
    def matriu_model(shader, x, y, z):
        model = pyrr.matrix44.create_from_translation(pyrr.Vector3([x, y, z]))
        model_loc = glGetUniformLocation(shader, "model")
        glUniformMatrix4fv(model_loc, 1, GL_FALSE, model)

    @staticmethod
    def matriu_view(shader, x, y, z):
        view = pyrr.matrix44.create_from_translation(pyrr.Vector3([x, y, z]))
        view_loc = glGetUniformLocation(shader, "view")
        glUniformMatrix4fv(view_loc, 1, GL_FALSE, view)

    @staticmethod
    def matrius_proj(shader, grau, w_width, w_height, near_pane, far_pane):
        proj = pyrr.matrix44.create_perspective_projection_matrix(grau, w_width / w_height, near_pane, far_pane)
        proj_loc = glGetUniformLocation(shader, "proj")
        glUniformMatrix4fv(proj_loc, 1, GL_FALSE, proj)
