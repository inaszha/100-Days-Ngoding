#include <GL/glut.h>
#include <cmath>

void DrawTriangle(void) {
    glPointSize(10);
    glBegin(GL_POINTS);

    // Titik 1 (Merah)
    glColor3f(1.0, 1.0, 0.0);
    glVertex2i(100, 100);

    // Titik 2 (Putih)
    glColor3f(1.0, 1.0, 1.0); // Putih
    glVertex2i(200, 100);

    // Titik 3 (Hijau)
    glColor3f(0.0, 1.0, 0.0); // Hijau
    // Hitung posisi titik hijau untuk membentuk segitiga sama sisi
    float x = 150.0;
    float y = 100.0 + sqrt(3) * 50;
    glVertex2f(x, y);

    glEnd();

    // Gambar garis segitiga
    glBegin(GL_LINE_LOOP);
    glColor3f(1.0, 1.0, 1.0); // Garis putih
    glVertex2i(100, 100);
    glVertex2i(200, 100);
    glVertex2f(x, y);
    glEnd();
}

void display(void) {
    glClear(GL_COLOR_BUFFER_BIT);
    DrawTriangle();
    glutSwapBuffers();
}

int main(int argc, char **argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitWindowPosition(100, 100);
    glutInitWindowSize(400, 300); // Lebar dan tinggi jendela yang diperbesar
    glutCreateWindow("Segitiga Sama Sisi by andri");
    glClearColor(0.0, 0.0, 0.0, 0.0);
    gluOrtho2D(0., 400., 0., 300.);
    glutDisplayFunc(display);
    glutMainLoop();
    return 0;
}
