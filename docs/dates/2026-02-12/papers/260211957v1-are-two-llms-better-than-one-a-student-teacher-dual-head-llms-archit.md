---
layout: default
title: Are Two LLMs Better Than One? A Student-Teacher Dual-Head LLMs Architecture for Pharmaceutical Content Optimization
---

# Are Two LLMs Better Than One? A Student-Teacher Dual-Head LLMs Architecture for Pharmaceutical Content Optimization
**arXiv**：[2602.11957v1](https://arxiv.org/abs/2602.11957) · [PDF](https://arxiv.org/pdf/2602.11957.pdf)  
**作者**：Suyash Mishra, Qiang Li, Anubhav Girdhar  

**一句话要点**：提出LRBTC架构，结合学生-教师双模型与人工循环，用于制药内容的质量控制与优化。

**关键词**：学生-教师架构, 内容质量控制, 制药合规, 语言模型应用, 人工循环工作流, 模块化质检

## 3 点简述
- 问题：制药领域内容需科学准确且合规，人工质检慢且易错，成为发布瓶颈。
- 方法：采用学生-教师双头LLMs架构，结合视觉语言模型和瀑布规则过滤，实现模块化质检。
- 效果：在AIReg-Bench上F1达83.0%，召回率97.5%，比Gemini 2.5 Pro漏检减少5倍；在CSpelling上平均准确率提升26.7%。

## 摘要（原文）

> Large language models (LLMs) are increasingly used to create content in regulated domains such as pharmaceuticals, where outputs must be scientifically accurate and legally compliant. Manual quality control (QC) is slow, error prone, and can become a publication bottleneck. We introduce LRBTC, a modular LLM and vision language model (VLM) driven QC architecture covering Language, Regulatory, Brand, Technical, and Content Structure checks. LRBTC combines a Student-Teacher dual model architecture, human in the loop (HITL) workflow with waterfall rule filtering to enable scalable, verifiable content validation and optimization. On AIReg-Bench, our approach achieves 83.0% F1 and 97.5% recall, reducing missed violations by 5x compared with Gemini 2.5 Pro. On CSpelling, it improves mean accuracy by 26.7%. Error analysis further reveals that while current models are strong at detecting misspellings (92.5 recall), they fail to identify complex medical grammatical (25.0 recall) and punctuation (41.7 recall) errors, highlighting a key area for future work. This work provides a practical, plug and play solution for reliable, transparent quality control of content in high stakes, compliance critical industries. We also provide access to our Demo under MIT Licenses.

