---
layout: default
title: Odysseus: Jailbreaking Commercial Multimodal LLM-integrated Systems via Dual Steganography
---

# Odysseus: Jailbreaking Commercial Multimodal LLM-integrated Systems via Dual Steganography
**arXiv**：[2512.20168v1](https://arxiv.org/abs/2512.20168) · [PDF](https://arxiv.org/pdf/2512.20168.pdf)  
**作者**：Songze Li, Jiameng Cheng, Yiming Li, Xiaojun Jia, Dacheng Tao  

**一句话要点**：提出Odysseus双隐写术以突破商业多模态大语言模型系统的安全过滤机制

**关键词**：多模态大语言模型, 越狱攻击, 隐写术, 安全过滤, 跨模态安全, 商业系统

## 3 点简述
- 核心问题：商业多模态大语言模型系统依赖显式内容检测，存在跨模态安全盲点。
- 方法要点：通过双隐写术在图像中隐蔽嵌入恶意查询与响应，规避过滤。
- 实验或效果：在基准数据集上对多个系统实现高达99%的攻击成功率。

## 摘要（原文）

> By integrating language understanding with perceptual modalities such as images, multimodal large language models (MLLMs) constitute a critical substrate for modern AI systems, particularly intelligent agents operating in open and interactive environments. However, their increasing accessibility also raises heightened risks of misuse, such as generating harmful or unsafe content. To mitigate these risks, alignment techniques are commonly applied to align model behavior with human values. Despite these efforts, recent studies have shown that jailbreak attacks can circumvent alignment and elicit unsafe outputs. Currently, most existing jailbreak methods are tailored for open-source models and exhibit limited effectiveness against commercial MLLM-integrated systems, which often employ additional filters. These filters can detect and prevent malicious input and output content, significantly reducing jailbreak threats. In this paper, we reveal that the success of these safety filters heavily relies on a critical assumption that malicious content must be explicitly visible in either the input or the output. This assumption, while often valid for traditional LLM-integrated systems, breaks down in MLLM-integrated systems, where attackers can leverage multiple modalities to conceal adversarial intent, leading to a false sense of security in existing MLLM-integrated systems. To challenge this assumption, we propose Odysseus, a novel jailbreak paradigm that introduces dual steganography to covertly embed malicious queries and responses into benign-looking images. Extensive experiments on benchmark datasets demonstrate that our Odysseus successfully jailbreaks several pioneering and realistic MLLM-integrated systems, achieving up to 99% attack success rate. It exposes a fundamental blind spot in existing defenses, and calls for rethinking cross-modal security in MLLM-integrated systems.

