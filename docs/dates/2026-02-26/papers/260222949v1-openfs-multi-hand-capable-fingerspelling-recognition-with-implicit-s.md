---
layout: default
title: OpenFS: Multi-Hand-Capable Fingerspelling Recognition with Implicit Signing-Hand Detection and Frame-Wise Letter-Conditioned Synthesis
---

# OpenFS: Multi-Hand-Capable Fingerspelling Recognition with Implicit Signing-Hand Detection and Frame-Wise Letter-Conditioned Synthesis
**arXiv**：[2602.22949v1](https://arxiv.org/abs/2602.22949) · [PDF](https://arxiv.org/pdf/2602.22949.pdf)  
**作者**：Junuk Cha, Jihyeon Kim, Han-Mu Park  

**一句话要点**：提出OpenFS方法，通过隐式手部检测和帧级字母条件合成解决手语拼写识别中的多手输入和词汇外问题。

**关键词**：手语拼写识别, 隐式手部检测, 多手输入, 帧级合成, 词汇外问题, 开源方法

## 3 点简述
- 核心问题：手语拼写识别存在手部歧义、训练损失不足和词汇外问题，传统方法依赖显式手部检测和CTC损失导致失败。
- 方法要点：开发多手兼容识别器，引入双级位置编码和手部聚焦损失进行隐式手部检测，使用单调对齐损失替代CTC损失，并设计帧级字母条件生成器合成新词汇。
- 实验或效果：通过综合实验验证方法在识别上达到先进性能，并构建FSNeo合成基准，代码和数据开源。

## 摘要（原文）

> Fingerspelling is a component of sign languages in which words are spelled out letter by letter using specific hand poses. Automatic fingerspelling recognition plays a crucial role in bridging the communication gap between Deaf and hearing communities, yet it remains challenging due to the signing-hand ambiguity issue, the lack of appropriate training losses, and the out-of-vocabulary (OOV) problem. Prior fingerspelling recognition methods rely on explicit signing-hand detection, which often leads to recognition failures, and on a connectionist temporal classification (CTC) loss, which exhibits the peaky behavior problem. To address these issues, we develop OpenFS, an open-source approach for fingerspelling recognition and synthesis. We propose a multi-hand-capable fingerspelling recognizer that supports both single- and multi-hand inputs and performs implicit signing-hand detection by incorporating a dual-level positional encoding and a signing-hand focus (SF) loss. The SF loss encourages cross-attention to focus on the signing hand, enabling implicit signing-hand detection during recognition. Furthermore, without relying on the CTC loss, we introduce a monotonic alignment (MA) loss that enforces the output letter sequence to follow the temporal order of the input pose sequence through cross-attention regularization. In addition, we propose a frame-wise letter-conditioned generator that synthesizes realistic fingerspelling pose sequences for OOV words. This generator enables the construction of a new synthetic benchmark, called FSNeo. Through comprehensive experiments, we demonstrate that our approach achieves state-of-the-art performance in recognition and validate the effectiveness of the proposed recognizer and generator. Codes and data are available in: https://github.com/JunukCha/OpenFS.

