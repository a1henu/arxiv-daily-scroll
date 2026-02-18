---
layout: default
title: UniTAF: A Modular Framework for Joint Text-to-Speech and Audio-to-Face Modeling
---

# UniTAF: A Modular Framework for Joint Text-to-Speech and Audio-to-Face Modeling
**arXiv**：[2602.15651v1](https://arxiv.org/abs/2602.15651) · [PDF](https://arxiv.org/pdf/2602.15651.pdf)  
**作者**：Qiangong Zhou, Nagasaka Tomohiro  

**一句话要点**：提出UniTAF框架，通过合并TTS和A2F模型实现内部特征传递，以提升文本生成音频与面部表情的一致性。

**关键词**：文本到语音, 音频到面部, 联合建模, 特征传递, 情感控制, 模块化框架

## 3 点简述
- 核心问题：独立TTS和A2F模型导致音频与面部表情生成不一致，需联合建模以改善协调性。
- 方法要点：设计模块化框架，将TTS和A2F合并为统一模型，支持中间特征重用和情感控制机制扩展。
- 实验或效果：从系统设计角度验证联合建模可行性，提供工程实践参考，未重点评估生成质量。

## 摘要（原文）

> This work considers merging two independent models, TTS and A2F, into a unified model to enable internal feature transfer, thereby improving the consistency between audio and facial expressions generated from text. We also discuss the extension of the emotion control mechanism from TTS to the joint model. This work does not aim to showcase generation quality; instead, from a system design perspective, it validates the feasibility of reusing intermediate representations from TTS for joint modeling of speech and facial expressions, and provides engineering practice references for subsequent speech expression co-design. The project code has been open source at: https://github.com/GoldenFishes/UniTAF

