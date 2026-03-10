---
layout: default
title: Invisible Safety Threat: Malicious Finetuning for LLM via Steganography
---

# Invisible Safety Threat: Malicious Finetuning for LLM via Steganography
**arXiv**：[2603.08104v1](https://arxiv.org/abs/2603.08104) · [PDF](https://arxiv.org/pdf/2603.08104.pdf)  
**作者**：Guangnian Wan, Xinyin Ma, Gongfan Fang, Xinchao Wang  

**一句话要点**：提出基于隐写术的恶意微调方法，揭示LLM在安全对齐下隐藏有害内容的风险。

**关键词**：大型语言模型安全, 隐写术攻击, 恶意微调, 安全对齐风险, 内容安全分类

## 3 点简述
- 核心问题：LLM安全对齐后仍可能通过隐写术隐蔽生成有害内容，威胁部署安全。
- 方法要点：微调模型理解隐写术，输入含隐藏恶意问题的提示，输出嵌入有害内容的良性响应。
- 实验或效果：在GPT-4.1和三个开源模型上验证攻击有效性，所有含恶意内容的隐写文本被误分类为安全。

## 摘要（原文）

> Understanding and addressing potential safety alignment risks in large language models (LLMs) is critical for ensuring their safe and trustworthy deployment. In this paper, we highlight an insidious safety threat: a compromised LLM can maintain a facade of proper safety alignment while covertly generating harmful content. To achieve this, we finetune the model to understand and apply a steganographic technique. At inference time, we input a prompt that contains a steganographically embedded malicious target question along with a plaintext cover question. The model, in turn, produces a target response similarly embedded within a benign-looking cover response. In this process, human observers only see the model being prompted with a cover question and generating a corresponding cover response, while the malicious content is hidden from view. We demonstrate this invisible safety threat on GPT-4.1 despite the OpenAI finetuning API's safeguards. The finetuned model produces steganographic malicious outputs in response to hidden malicious prompts, while the user interface displays only a fully benign cover interaction. We also replicate the attack on three open-source models, Llama-3.3-70B-Instruct, Phi-4, and Mistral-Small-24B-Base-2501, confirming the generality of our method. We quantitatively evaluate our method on the AdvBench dataset, using Llama-Guard-3-8B for content safety classification. Across all four models, all stegotexts containing malicious content are incorrectly classified as safe.

