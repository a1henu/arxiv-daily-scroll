---
layout: default
title: NVIDIA Nemotron Parse 1.1
---

# NVIDIA Nemotron Parse 1.1
**arXiv**：[2511.20478v1](https://arxiv.org/abs/2511.20478) · [PDF](https://arxiv.org/pdf/2511.20478.pdf)  
**作者**：Kateryna Chumachenko, Amala Sanjay Deshmukh, Jarno Seppanen, Ilia Karmanov, Chia-Chih Chen, Lukas Voegtle, Philipp Fischer, Marek Wawrzos, Saeid Motiian, Roman Ageev, Kedi Wu, Alexandre Milesi, Maryam Moosaei, Krzysztof Pawelec, Padmavathy Subramanian, Mehrzad Samadi, Xin Yu, Celina Dear, Sarah Stoddard, Jenna Diamond, Jesse Oliver, Leanna Chraghchian, Patrick Skelly, Tom Balough, Yao Xu, Jane Polak Scowcroft, Daniel Korzekwa, Darragh Hanley, Sandip Bhaskar, Timo Roman, Karan Sapra, Andrew Tao, Bryan Catanzaro  

**一句话要点**：提出Nemotron-Parse-1.1轻量文档解析模型，提升OCR、表格解析和图表文本提取能力。

**关键词**：文档解析, OCR模型, 表格解析, 轻量架构, 编码器-解码器

## 3 点简述
- 核心问题：轻量文档解析需高效处理OCR、表格和图表文本，支持长序列输出。
- 方法要点：采用编码器-解码器架构，参数量885M，包括紧凑语言解码器。
- 实验或效果：在公共基准上实现竞争性准确率，并发布优化版本提升速度。

## 摘要（原文）

> We introduce Nemotron-Parse-1.1, a lightweight document parsing and OCR model that advances the capabilities of its predecessor, Nemoretriever-Parse-1.0. Nemotron-Parse-1.1 delivers improved capabilities across general OCR, markdown formatting, structured table parsing, and text extraction from pictures, charts, and diagrams. It also supports a longer output sequence length for visually dense documents. As with its predecessor, it extracts bounding boxes of text segments, as well as corresponding semantic classes. Nemotron-Parse-1.1 follows an encoder-decoder architecture with 885M parameters, including a compact 256M-parameter language decoder. It achieves competitive accuracy on public benchmarks making it a strong lightweight OCR solution. We release the model weights publicly on Huggingface, as well as an optimized NIM container, along with a subset of the training data as part of the broader Nemotron-VLM-v2 dataset. Additionally, we release Nemotron-Parse-1.1-TC which operates on a reduced vision token length, offering a 20% speed improvement with minimal quality degradation.

