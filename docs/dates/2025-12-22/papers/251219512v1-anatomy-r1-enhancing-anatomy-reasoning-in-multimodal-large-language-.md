---
layout: default
title: Anatomy-R1: Enhancing Anatomy Reasoning in Multimodal Large Language Models via Anatomical Similarity Curriculum and Group Diversity Augmentation
---

# Anatomy-R1: Enhancing Anatomy Reasoning in Multimodal Large Language Models via Anatomical Similarity Curriculum and Group Diversity Augmentation
**arXiv**：[2512.19512v1](https://arxiv.org/abs/2512.19512) · [PDF](https://arxiv.org/pdf/2512.19512.pdf)  
**作者**：Ziyang Song, Zelin Zang, Zuyao Chen, Xusheng Liang, Dong Yi, Jinlin Wu, Hongbin Liu, Jiebo Luo  

**一句话要点**：提出解剖相似性课程学习和组多样性问题增强，以提升多模态大语言模型在医学解剖图像中的推理能力。

**关键词**：多模态大语言模型, 医学图像理解, 解剖推理, 课程学习, 问题增强, 监督微调

## 3 点简述
- 核心问题：传统监督微调在医学解剖图像理解中效果有限，GRPO方法存在知识共享不均和推理路径单一的问题。
- 方法要点：通过解剖相似性课程学习渐进控制问题难度，利用组多样性问题增强扩展模型搜索空间。
- 实验或效果：在SGG-VQA和OmniMedVQA基准测试中显著提升性能，验证了方法的有效性。

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) have achieved impressive progress in natural image reasoning, yet their potential in medical imaging remains underexplored, especially in clinical anatomical surgical images. Anatomy understanding tasks demand precise understanding and clinically coherent answers, which are difficult to achieve due to the complexity of medical data and the scarcity of high-quality expert annotations. These challenges limit the effectiveness of conventional Supervised Fine-Tuning (SFT) strategies. While recent work has demonstrated that Group Relative Policy Optimization (GRPO) can enhance reasoning in MLLMs without relying on large amounts of data, we find two weaknesses that hinder GRPO's reasoning performance in anatomy recognition: 1) knowledge cannot be effectively shared between different anatomical structures, resulting in uneven information gain and preventing the model from converging, and 2) the model quickly converges to a single reasoning path, suppressing the exploration of diverse strategies. To overcome these challenges, we propose two novel methods. First, we implement a progressive learning strategy called Anatomical Similarity Curriculum Learning by controlling question difficulty via the similarity of answer choices, enabling the model to master complex problems incrementally. Second, we utilize question augmentation referred to as Group Diversity Question Augmentation to expand the model's search space for difficult queries, mitigating the tendency to produce uniform responses. Comprehensive experiments on the SGG-VQA and OmniMedVQA benchmarks show our method achieves a significant improvement across the two benchmarks, demonstrating its effectiveness in enhancing the medical reasoning capabilities of MLLMs. The code can be found in https://github.com/tomato996/Anatomy-R1

