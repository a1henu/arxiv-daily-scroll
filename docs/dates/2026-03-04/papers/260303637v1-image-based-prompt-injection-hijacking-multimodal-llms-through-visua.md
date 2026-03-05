---
layout: default
title: Image-based Prompt Injection: Hijacking Multimodal LLMs through Visually Embedded Adversarial Instructions
---

# Image-based Prompt Injection: Hijacking Multimodal LLMs through Visually Embedded Adversarial Instructions
**arXiv**：[2603.03637v1](https://arxiv.org/abs/2603.03637) · [PDF](https://arxiv.org/pdf/2603.03637.pdf)  
**作者**：Neha Nagaraja, Lan Zhang, Zhilong Wang, Bo Zhang, Pawan Patil  

**一句话要点**：提出图像提示注入攻击以揭示多模态大语言模型的黑盒漏洞

**关键词**：多模态大语言模型, 图像提示注入, 黑盒攻击, 对抗指令, 视觉安全, 模型漏洞

## 3 点简述
- 研究多模态大语言模型因视觉文本融合引入的图像提示注入漏洞
- 开发基于分割、自适应字体和背景感知的端到端攻击流水线以隐蔽嵌入对抗指令
- 在COCO数据集上评估12种策略，最高攻击成功率64%，突显黑盒威胁

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) integrate vision and text to power applications, but this integration introduces new vulnerabilities. We study Image-based Prompt Injection (IPI), a black-box attack in which adversarial instructions are embedded into natural images to override model behavior. Our end-to-end IPI pipeline incorporates segmentation-based region selection, adaptive font scaling, and background-aware rendering to conceal prompts from human perception while preserving model interpretability. Using the COCO dataset and GPT-4-turbo, we evaluate 12 adversarial prompt strategies and multiple embedding configurations. The results show that IPI can reliably manipulate the output of the model, with the most effective configuration achieving up to 64\% attack success under stealth constraints. These findings highlight IPI as a practical threat in black-box settings and underscore the need for defenses against multimodal prompt injection.

