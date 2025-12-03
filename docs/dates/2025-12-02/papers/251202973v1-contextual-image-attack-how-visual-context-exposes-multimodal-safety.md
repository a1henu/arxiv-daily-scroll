---
layout: default
title: Contextual Image Attack: How Visual Context Exposes Multimodal Safety Vulnerabilities
---

# Contextual Image Attack: How Visual Context Exposes Multimodal Safety Vulnerabilities
**arXiv**：[2512.02973v1](https://arxiv.org/abs/2512.02973) · [PDF](https://arxiv.org/pdf/2512.02973.pdf)  
**作者**：Yuan Xiong, Ziqi Miao, Lijun Li, Chen Qian, Jie Li, Jing Shao  

**一句话要点**：提出Contextual Image Attack，通过视觉上下文嵌入有害查询以攻击多模态大语言模型安全对齐。

**关键词**：多模态大语言模型, 安全对齐, 视觉上下文攻击, 多代理系统, 毒性评估

## 3 点简述
- 核心问题：现有攻击方法未充分利用图像携带复杂上下文信息的潜力，视觉模态安全漏洞显著。
- 方法要点：采用多代理系统，通过四种可视化策略将有害查询嵌入良性视觉上下文，结合元素增强和毒性混淆技术。
- 实验或效果：在MMSafetyBench-tiny数据集上，对GPT-4o和Qwen2.5-VL-72B模型毒性得分高，攻击成功率超过86%。

## 摘要（原文）

> While Multimodal Large Language Models (MLLMs) show remarkable capabilities, their safety alignments are susceptible to jailbreak attacks. Existing attack methods typically focus on text-image interplay, treating the visual modality as a secondary prompt. This approach underutilizes the unique potential of images to carry complex, contextual information. To address this gap, we propose a new image-centric attack method, Contextual Image Attack (CIA), which employs a multi-agent system to subtly embeds harmful queries into seemingly benign visual contexts using four distinct visualization strategies. To further enhance the attack's efficacy, the system incorporate contextual element enhancement and automatic toxicity obfuscation techniques. Experimental results on the MMSafetyBench-tiny dataset show that CIA achieves high toxicity scores of 4.73 and 4.83 against the GPT-4o and Qwen2.5-VL-72B models, respectively, with Attack Success Rates (ASR) reaching 86.31\% and 91.07\%. Our method significantly outperforms prior work, demonstrating that the visual modality itself is a potent vector for jailbreaking advanced MLLMs.

