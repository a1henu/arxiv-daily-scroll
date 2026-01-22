---
layout: default
title: DeepMoLM: Leveraging Visual and Geometric Structural Information for Molecule-Text Modeling
---

# DeepMoLM: Leveraging Visual and Geometric Structural Information for Molecule-Text Modeling
**arXiv**：[2601.14732v1](https://arxiv.org/abs/2601.14732) · [PDF](https://arxiv.org/pdf/2601.14732.pdf)  
**作者**：Jing Lan, Hexiao Ding, Hongzhao Chen, Yufeng Jiang, Nga-Chun Ng, Gwing Kei Yip, Gerald W. Y. Cheng, Yunlin Mao, Jing Cai, Liang-ting Lin, Jung Sun Yoo  

**一句话要点**：提出DeepMoLM框架，通过融合视觉与几何结构信息提升分子-文本建模性能

**关键词**：分子-文本建模, 双视图框架, 几何不变量, 交叉注意力, 立体化学, 药物发现

## 3 点简述
- 核心问题：现有分子语言模型依赖字符串或图结构，视觉语言模型常忽略立体化学细节，难以将连续3D结构映射为离散标记。
- 方法要点：采用双视图框架，结合高分辨率分子图像和基于分子构象的几何不变量，通过交叉注意力融合视觉与几何流。
- 实验或效果：在PubChem描述生成中相对最强通用基线提升12.3% METEOR，在ChEBI-20图像描述生成中超越通用基线并匹配先进视觉语言模型。

## 摘要（原文）

> AI models for drug discovery and chemical literature mining must interpret molecular images and generate outputs consistent with 3D geometry and stereochemistry. Most molecular language models rely on strings or graphs, while vision-language models often miss stereochemical details and struggle to map continuous 3D structures into discrete tokens. We propose DeepMoLM: Deep Molecular Language M odeling, a dual-view framework that grounds high-resolution molecular images in geometric invariants derived from molecular conformations. DeepMoLM preserves high-frequency evidence from 1024 $\times$ 1024 inputs, encodes conformer neighborhoods as discrete Extended 3-Dimensional Fingerprints, and fuses visual and geometric streams with cross-attention, enabling physically grounded generation without atom coordinates. DeepMoLM improves PubChem captioning with a 12.3% relative METEOR gain over the strongest generalist baseline while staying competitive with specialist methods. It produces valid numeric outputs for all property queries and attains MAE 13.64 g/mol on Molecular Weight and 37.89 on Complexity in the specialist setting. On ChEBI-20 description generation from images, it exceeds generalist baselines and matches state-of-the-art vision-language models. Code is available at https://github.com/1anj/DeepMoLM.

