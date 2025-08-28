# P0: Automatisk Pointberegning til King Domino

## Projektoversigt
Dette repository indeholder p0-projektet, der fokuserer på udvikling af et automatisk pointberegningssystem til brætspillet *King Domino*.
Projektets primære mål er at beregne spilpoint ud fra billeder af spilplader ved hjælp af to forskellige tekniske tilgange.

## Projektformål
- Udvikle et program, der automatisk beregner point i *King Domino* baseret på visuel input
- to tekniske metoder:
  1. **Udvidelse af professor Andreas Moegelmose's basisløsning** (uden genkendelse af kroner på brikker)
  2. **Implementering af Meta's Detectron2-model til panoptic segmentering** (inkl. kronegenkendelse)

## Om King Domino
*King Domino* er et strategisk brætspil, hvor spillerne bygger kongeriger ved hjælp af farvede dominobrikker. Vinderen findes ved højeste pointsum ved spillets afslutning. Point beregnes baseret på:
- Mønstre i brikplaceringer
- Sammenhængende områder med ens farver
- Strategisk placering af kronesymboler på brikker

## Teknisk Tilgang
### Metode 1: Basisløsning
- Bygger videre på professor Andreas Moegelmose's eksisterende implementation
- Fokuserer på kernefunktionalitet til brikgenkendelse og pointberegning
- *Begrænsning: Behandler ikke kroner på brikker*

### Metode 2: Detectron2-implementering
- Anvender Meta's Detectron2-framework til panoptic segmentering
- Håndterer både brikidentifikation og kronegenkendelse
- *Fordele: Komplet funktionalitet inkl. kroner*

## Repository-struktur

kommmer når færdig.
