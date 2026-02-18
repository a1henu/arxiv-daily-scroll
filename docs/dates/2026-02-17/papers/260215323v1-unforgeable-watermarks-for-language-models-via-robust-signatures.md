---
layout: default
title: Unforgeable Watermarks for Language Models via Robust Signatures
---

# Unforgeable Watermarks for Language Models via Robust Signatures
**arXiv**：[2602.15323v1](https://arxiv.org/abs/2602.15323) · [PDF](https://arxiv.org/pdf/2602.15323.pdf)  
**作者**：Huijia Lin, Kameron Shahabi, Min Jae Song  

**一句话要点**：提出基于鲁棒签名的不可伪造水印方案，以增强语言模型内容溯源的安全性。

**关键词**：语言模型水印, 鲁棒签名, 内容溯源, 不可伪造性, 可恢复性, 汉明度量

## 3 点简述
- 核心问题：现有水印方案在防止虚假归属方面保护有限，需强化内容所有权验证。
- 方法要点：引入不可伪造性和可恢复性保证，利用鲁棒数字签名构造抗替换攻击的水印方案。
- 实验或效果：方案在汉明度量下实现鲁棒、不可伪造和可恢复，提升安全归属和细粒度可追溯性。

## 摘要（原文）

> Language models now routinely produce text that is difficult to distinguish from human writing, raising the need for robust tools to verify content provenance. Watermarking has emerged as a promising countermeasure, with existing work largely focused on model quality preservation and robust detection. However, current schemes provide limited protection against false attribution. We strengthen the notion of soundness by introducing two novel guarantees: unforgeability and recoverability. Unforgeability prevents adversaries from crafting false positives, texts that are far from any output from the watermarked model but are nonetheless flagged as watermarked. Recoverability provides an additional layer of protection: whenever a watermark is detected, the detector identifies the source text from which the flagged content was derived. Together, these properties strengthen content ownership by linking content exclusively to its generating model, enabling secure attribution and fine-grained traceability. We construct the first undetectable watermarking scheme that is robust, unforgeable, and recoverable with respect to substitutions (i.e., perturbations in Hamming metric). The key technical ingredient is a new cryptographic primitive called robust (or recoverable) digital signatures, which allow verification of messages that are close to signed ones, while preventing forgery of messages that are far from all previously signed messages. We show that any standard digital signature scheme can be boosted to a robust one using property-preserving hash functions (Boyle, LaVigne, and Vaikuntanathan, ITCS 2019).

