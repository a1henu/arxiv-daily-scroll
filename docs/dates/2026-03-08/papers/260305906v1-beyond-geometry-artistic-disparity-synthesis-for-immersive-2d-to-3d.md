---
layout: default
title: Beyond Geometry: Artistic Disparity Synthesis for Immersive 2D-to-3D
---

# Beyond Geometry: Artistic Disparity Synthesis for Immersive 2D-to-3D
**arXiv**：[2603.05906v1](https://arxiv.org/abs/2603.05906) · [PDF](https://arxiv.org/pdf/2603.05906.pdf)  
**作者**：Ping Chen, Zezhou Chen, Xingpeng Zhang, Yanlin Qian, Huan Hu, Xiang Liu, Zipeng Wang, Xin Wang, Zhaoxiang Liu, Kai Wang, Shiguo Lian  

**一句话要点**：提出Art3D框架以解决2D转3D中艺术性不足的问题，通过艺术视差合成提升沉浸感。

**关键词**：艺术视差合成, 2D转3D, 沉浸式体验, 双路径架构, 间接监督, 电影对齐评估

## 3 点简述
- 核心问题：现有2D转3D方法几何准确但艺术性差，无法复制专业3D电影的情感共鸣体验。
- 方法要点：采用双路径架构解耦全局深度参数与局部艺术效果，通过间接监督学习专业3D电影数据。
- 实验或效果：初步实验显示能复制关键局部出屏效果，并与电影3D内容的全局深度风格对齐。

## 摘要（原文）

> Current 2D-to-3D conversion methods achieve geometric accuracy but are artistically deficient, failing to replicate the immersive and emotionally resonant experience of professional 3D cinema. This is because geometric reconstruction paradigms mistake deliberate artistic intent, such as strategic zero-plane shifts for pop-out effects and local depth sculpting, for data noise or ambiguity. This paper argues for a new paradigm: Artistic Disparity Synthesis, shifting the goal from physically accurate disparity estimation to artistically coherent disparity synthesis. We propose Art3D, a preliminary framework exploring this paradigm. Art3D uses a dual-path architecture to decouple global depth parameters (macro-intent) from local artistic effects (visual brushstrokes) and learns from professional 3D film data via indirect supervision. We also introduce a preliminary evaluation method to quantify cinematic alignment. Experiments show our approach demonstrates potential in replicating key local out-of-screen effects and aligning with the global depth styles of cinematic 3D content, laying the groundwork for a new class of artistically-driven conversion tools.

