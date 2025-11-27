---
layout: default
title: EM-KD: Distilling Efficient Multimodal Large Language Model with Unbalanced Vision Tokens
---

# EM-KD: Distilling Efficient Multimodal Large Language Model with Unbalanced Vision Tokens
**arXiv**：[2511.21106v1](https://arxiv.org/abs/2511.21106) · [PDF](https://arxiv.org/pdf/2511.21106.pdf)  
**作者**：Ze Feng, Sen Yang, Boqiang Duan, Wankou Yang, Jingdong Wang  

**一句话要点**：提出EM-KD以解决高效多模态大模型中视觉令牌不平衡导致的细粒度理解下降问题

**关键词**：知识蒸馏, 多模态大语言模型, 视觉令牌对齐, 高效计算, 语义理解

## 3 点简述
- 核心问题：高效多模态大模型压缩视觉令牌时，令牌不平衡导致细粒度视觉理解能力下降
- 方法要点：使用匈牙利算法对齐师生视觉令牌，并引入亲和力与语义蒸馏策略
- 实验或效果：在多个基准测试中，EM-KD在准确性和效率上显著优于先前方法

## 摘要（原文）

> Efficient Multimodal Large Language Models (MLLMs) compress vision tokens to reduce resource consumption, but the loss of visual information can degrade comprehension capabilities. Although some priors introduce Knowledge Distillation to enhance student models, they overlook the fundamental differences in fine-grained vision comprehension caused by unbalanced vision tokens between the efficient student and vanilla teacher. In this paper, we propose EM-KD, a novel paradigm that enhances the Efficient MLLMs with Knowledge Distillation. To overcome the challenge of unbalanced vision tokens, we first calculate the Manhattan distance between the vision logits of teacher and student, and then align them in the spatial dimension with the Hungarian matching algorithm. After alignment, EM-KD introduces two distillation strategies: 1) Vision-Language Affinity Distillation (VLAD) and 2) Vision Semantic Distillation (VSD). Specifically, VLAD calculates the affinity matrix between text tokens and aligned vision tokens, and minimizes the smooth L1 distance of the student and the teacher affinity matrices. Considering the semantic richness of vision logits in the final layer, VSD employs the reverse KL divergence to measure the discrete probability distributions of the aligned vision logits over the vocabulary space. Comprehensive evaluation on diverse benchmarks demonstrates that EM-KD trained model outperforms prior Efficient MLLMs on both accuracy and efficiency with a large margin, validating its effectiveness. Compared with previous distillation methods, which are equipped with our proposed vision token matching strategy for fair comparison, EM-KD also achieves better performance.

