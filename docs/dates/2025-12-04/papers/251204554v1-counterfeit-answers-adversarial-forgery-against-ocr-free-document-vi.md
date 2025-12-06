---
layout: default
title: Counterfeit Answers: Adversarial Forgery against OCR-Free Document Visual Question Answering
---

# Counterfeit Answers: Adversarial Forgery against OCR-Free Document Visual Question Answering
**arXiv**：[2512.04554v1](https://arxiv.org/abs/2512.04554) · [PDF](https://arxiv.org/pdf/2512.04554.pdf)  
**作者**：Marco Pintore, Maura Pintor, Dimosthenis Karatzas, Battista Biggio  

**一句话要点**：提出针对OCR-Free文档视觉问答的对抗伪造攻击，以诱导模型错误答案

**关键词**：文档视觉问答, 对抗攻击, OCR-Free模型, 视觉伪造, 模型鲁棒性

## 3 点简述
- 核心问题：OCR-Free文档视觉问答模型易受对抗攻击，导致语义误导或系统失效
- 方法要点：开发专门攻击算法，生成视觉不可察觉但语义针对性的伪造文档
- 实验或效果：在Pix2Struct和Donut等先进模型上验证攻击有效性，揭示系统脆弱性

## 摘要（原文）

> Document Visual Question Answering (DocVQA) enables end-to-end reasoning grounded on information present in a document input. While recent models have shown impressive capabilities, they remain vulnerable to adversarial attacks. In this work, we introduce a novel attack scenario that aims to forge document content in a visually imperceptible yet semantically targeted manner, allowing an adversary to induce specific or generally incorrect answers from a DocVQA model. We develop specialized attack algorithms that can produce adversarially forged documents tailored to different attackers' goals, ranging from targeted misinformation to systematic model failure scenarios. We demonstrate the effectiveness of our approach against two end-to-end state-of-the-art models: Pix2Struct, a vision-language transformer that jointly processes image and text through sequence-to-sequence modeling, and Donut, a transformer-based model that directly extracts text and answers questions from document images. Our findings highlight critical vulnerabilities in current DocVQA systems and call for the development of more robust defenses.

