---
layout: default
title: Art2Mus: Artwork-to-Music Generation via Visual Conditioning and Large-Scale Cross-Modal Alignment
---

# Art2Mus: Artwork-to-Music Generation via Visual Conditioning and Large-Scale Cross-Modal Alignment
**arXiv**：[2602.17599v1](https://arxiv.org/abs/2602.17599) · [PDF](https://arxiv.org/pdf/2602.17599.pdf)  
**作者**：Ivan Rinaldi, Matteo Mendula, Nicola Fanelli, Florence Levé, Matteo Testi, Giovanna Castellano, Gennaro Vessio  

**一句话要点**：提出ArtToMus框架，通过视觉条件化和跨模态对齐实现艺术品到音乐的生成。

**关键词**：艺术品到音乐生成, 视觉条件化, 跨模态对齐, 潜在扩散模型, 大规模数据集

## 3 点简述
- 现有图像条件音乐生成系统依赖自然照片和图像到文本转换，限制了艺术品语义和风格的捕捉。
- ArtToMus框架直接映射艺术品视觉嵌入到潜在扩散模型，无需语言中介，实现视觉到音乐的生成。
- 实验显示ArtToMus生成音乐与艺术品风格一致，跨模态对齐分数虽低于文本条件系统，但感知质量竞争。

## 摘要（原文）

> Music generation has advanced markedly through multimodal deep learning, enabling models to synthesize audio from text and, more recently, from images. However, existing image-conditioned systems suffer from two fundamental limitations: (i) they are typically trained on natural photographs, limiting their ability to capture the richer semantic, stylistic, and cultural content of artworks; and (ii) most rely on an image-to-text conversion stage, using language as a semantic shortcut that simplifies conditioning but prevents direct visual-to-audio learning. Motivated by these gaps, we introduce ArtSound, a large-scale multimodal dataset of 105,884 artwork-music pairs enriched with dual-modality captions, obtained by extending ArtGraph and the Free Music Archive. We further propose ArtToMus, the first framework explicitly designed for direct artwork-to-music generation, which maps digitized artworks to music without image-to-text translation or language-based semantic supervision. The framework projects visual embeddings into the conditioning space of a latent diffusion model, enabling music synthesis guided solely by visual information. Experimental results show that ArtToMus generates musically coherent and stylistically consistent outputs that reflect salient visual cues of the source artworks. While absolute alignment scores remain lower than those of text-conditioned systems-as expected given the substantially increased difficulty of removing linguistic supervision-ArtToMus achieves competitive perceptual quality and meaningful cross-modal correspondence. This work establishes direct visual-to-music generation as a distinct and challenging research direction, and provides resources that support applications in multimedia art, cultural heritage, and AI-assisted creative practice. Code and dataset will be publicly released upon acceptance.

