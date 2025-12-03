---
layout: default
title: Diagnose, Correct, and Learn from Manipulation Failures via Visual Symbols
---

# Diagnose, Correct, and Learn from Manipulation Failures via Visual Symbols
**arXiv**：[2512.02787v1](https://arxiv.org/abs/2512.02787) · [PDF](https://arxiv.org/pdf/2512.02787.pdf)  
**作者**：Xianchao Zeng, Xinyu Zhou, Youcheng Li, Jiayou Shi, Tianle Li, Liangming Chen, Lei Ren, Yong-Lu Li  

**一句话要点**：提出ViFailback框架以诊断机器人操作失败并提供视觉符号引导

**关键词**：机器人操作失败诊断, 视觉符号引导, 视觉问答数据集, 视觉语言模型基准, 真实世界泛化

## 3 点简述
- 核心问题：VLA模型在失败诊断与学习方面受限，现有数据集模拟生成泛化性差
- 方法要点：利用视觉符号增强标注效率，构建大规模真实世界VQA数据集与基准测试
- 实验或效果：ViFailback-8B模型在基准测试中表现优异，集成VLA模型实现真实世界失败恢复

## 摘要（原文）

> Vision-Language-Action (VLA) models have recently achieved remarkable progress in robotic manipulation, yet they remain limited in failure diagnosis and learning from failures. Additionally, existing failure datasets are mostly generated programmatically in simulation, which limits their generalization to the real world. In light of these, we introduce ViFailback, a framework designed to diagnose robotic manipulation failures and provide both textual and visual correction guidance. Our framework utilizes explicit visual symbols to enhance annotation efficiency. We further release the ViFailback dataset, a large-scale collection of 58,126 Visual Question Answering (VQA) pairs along with their corresponding 5,202 real-world manipulation trajectories. Based on the dataset, we establish ViFailback-Bench, a benchmark of 11 fine-grained VQA tasks designed to assess the failure diagnosis and correction abilities of Vision-Language Models (VLMs), featuring ViFailback-Bench Lite for closed-ended and ViFailback-Bench Hard for open-ended evaluation. To demonstrate the effectiveness of our framework, we built the ViFailback-8B VLM, which not only achieves significant overall performance improvement on ViFailback-Bench but also generates visual symbols for corrective action guidance. Finally, by integrating ViFailback-8B with a VLA model, we conduct real-world robotic experiments demonstrating its ability to assist the VLA model in recovering from failures. Project Website: https://x1nyuzhou.github.io/vifailback.github.io/

