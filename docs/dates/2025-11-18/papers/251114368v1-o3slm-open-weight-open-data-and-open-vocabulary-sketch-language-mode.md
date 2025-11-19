---
layout: default
title: O3SLM: Open Weight, Open Data, and Open Vocabulary Sketch-Language Model
---

# O3SLM: Open Weight, Open Data, and Open Vocabulary Sketch-Language Model
**arXiv**：[2511.14368v1](https://arxiv.org/abs/2511.14368) · [PDF](https://arxiv.org/pdf/2511.14368.pdf)  
**作者**：Rishi Gupta, Mukilan Karuppasamy, Shyam Marjit, Aditay Tripathi, Anirban Chakraborty  

**一句话要点**：提出O3SLM模型与数据集以解决大视觉语言模型在草图理解上的瓶颈

**关键词**：草图语言模型, 大规模数据集, 视觉语言理解, 草图视觉问答, 多模态学习

## 3 点简述
- 核心问题：大视觉语言模型难以理解手绘草图等抽象视觉输入，缺乏大规模草图-图像-指令数据集。
- 方法要点：构建大规模图像-草图-指令三元组数据集，并训练O3SLM模型进行预训练和指令调优。
- 实验或效果：在草图定位、计数、检索和VQA任务中，O3SLM实现SOTA性能，显著优于现有模型。

## 摘要（原文）

> While Large Vision Language Models (LVLMs) are increasingly deployed in real-world applications, their ability to interpret abstract visual inputs remains limited. Specifically, they struggle to comprehend hand-drawn sketches, a modality that offers an intuitive means of expressing concepts that are difficult to describe textually. We identify the primary bottleneck as the absence of a large-scale dataset that jointly models sketches, photorealistic images, and corresponding natural language instructions. To address this, we present two key contributions: (1) a new, large-scale dataset of image-sketch-instruction triplets designed to facilitate both pretraining and instruction tuning, and (2) O3SLM, an LVLM trained on this dataset. Comprehensive evaluations on multiple sketch-based tasks: (a) object localization, (b) counting, (c) image retrieval i.e., (SBIR and fine-grained SBIR), and (d) visual question answering (VQA); while incorporating the three existing sketch datasets, namely QuickDraw!, Sketchy, and Tu Berlin, along with our generated SketchVCL dataset, show that O3SLM achieves state-of-the-art performance, substantially outperforming existing LVLMs in sketch comprehension and reasoning.

