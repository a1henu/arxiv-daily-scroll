---
layout: default
title: Hierarchical Modeling Approach to Fast and Accurate Table Recognition
---

# Hierarchical Modeling Approach to Fast and Accurate Table Recognition
**arXiv**：[2512.21083v1](https://arxiv.org/abs/2512.21083) · [PDF](https://arxiv.org/pdf/2512.21083.pdf)  
**作者**：Takaya Kawakatsu  

**一句话要点**：提出基于非因果注意力的多任务模型与并行推理算法，以加速表格识别并提升准确性。

**关键词**：表格识别, 多任务学习, 非因果注意力, 并行推理, 文档理解

## 3 点简述
- 表格识别包含结构、位置和内容三个子任务，现有方法推理慢且有效性未充分解释。
- 采用非因果注意力捕获全局表格结构，结合多任务学习与并行算法加速内容推理。
- 在两个大型公开数据集上，通过视觉和统计评估验证了方法的优越性。

## 摘要（原文）

> The extraction and use of diverse knowledge from numerous documents is a pressing challenge in intelligent information retrieval. Documents contain elements that require different recognition methods. Table recognition typically consists of three subtasks, namely table structure, cell position and cell content recognition. Recent models have achieved excellent recognition with a combination of multi-task learning, local attention, and mutual learning. However, their effectiveness has not been fully explained, and they require a long period of time for inference. This paper presents a novel multi-task model that utilizes non-causal attention to capture the entire table structure, and a parallel inference algorithm for faster cell content inference. The superiority is demonstrated both visually and statistically on two large public datasets.

