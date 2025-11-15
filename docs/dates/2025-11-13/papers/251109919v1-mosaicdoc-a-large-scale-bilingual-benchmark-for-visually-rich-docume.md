---
layout: default
title: MosaicDoc: A Large-Scale Bilingual Benchmark for Visually Rich Document Understanding
---

# MosaicDoc: A Large-Scale Bilingual Benchmark for Visually Rich Document Understanding
**arXiv**：[2511.09919v1](https://arxiv.org/abs/2511.09919) · [PDF](https://arxiv.org/pdf/2511.09919.pdf)  
**作者**：Ketong Chen, Yuhao Chen, Yang Xue  

**一句话要点**：提出MosaicDoc双语基准以解决视觉丰富文档理解评估不足问题

**关键词**：视觉丰富文档理解, 双语基准, 多任务标注, 自动生成, 复杂布局

## 3 点简述
- 现有基准多为英语、布局简单，无法评估复杂文档理解能力
- 使用DocWeaver多智能体流程自动生成大规模双语数据集
- 评估显示先进模型在处理真实文档复杂性方面存在局限

## 摘要（原文）

> Despite the rapid progress of Vision-Language Models (VLMs), their capabilities are inadequately assessed by existing benchmarks, which are predominantly English-centric, feature simplistic layouts, and support limited tasks. Consequently, they fail to evaluate model performance for Visually Rich Document Understanding (VRDU), a critical challenge involving complex layouts and dense text. To address this, we introduce DocWeaver, a novel multi-agent pipeline that leverages Large Language Models to automatically generate a new benchmark. The result is MosaicDoc, a large-scale, bilingual (Chinese and English) resource designed to push the boundaries of VRDU. Sourced from newspapers and magazines, MosaicDoc features diverse and complex layouts (including multi-column and non-Manhattan), rich stylistic variety from 196 publishers, and comprehensive multi-task annotations (OCR, VQA, reading order, and localization). With 72K images and over 600K QA pairs, MosaicDoc serves as a definitive benchmark for the field. Our extensive evaluation of state-of-the-art models on this benchmark reveals their current limitations in handling real-world document complexity and charts a clear path for future research.

