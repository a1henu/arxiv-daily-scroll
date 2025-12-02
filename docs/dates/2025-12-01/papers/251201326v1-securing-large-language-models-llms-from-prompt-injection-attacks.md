---
layout: default
title: Securing Large Language Models (LLMs) from Prompt Injection Attacks
---

# Securing Large Language Models (LLMs) from Prompt Injection Attacks
**arXiv**：[2512.01326v1](https://arxiv.org/abs/2512.01326) · [PDF](https://arxiv.org/pdf/2512.01326.pdf)  
**作者**：Omar Farooq Khan Suri, John McCrae  

**一句话要点**：评估JATMO防御方法对HOUYI攻击的鲁棒性，揭示微调防御的局限与权衡

**关键词**：提示注入攻击, 大语言模型安全, 微调防御, 遗传攻击框架, 鲁棒性评估

## 3 点简述
- 核心问题：LLMs易受提示注入攻击，利用指令跟随能力执行恶意任务。
- 方法要点：采用JATMO任务特定微调，并基于HOUYI攻击框架评估其防御效果。
- 实验或效果：JATMO降低攻击成功率但未完全阻止，存在生成质量与漏洞的权衡。

## 摘要（原文）

> Large Language Models (LLMs) are increasingly being deployed in real-world applications, but their flexibility exposes them to prompt injection attacks. These attacks leverage the model's instruction-following ability to make it perform malicious tasks. Recent work has proposed JATMO, a task-specific fine-tuning approach that trains non-instruction-tuned base models to perform a single function, thereby reducing susceptibility to adversarial instructions. In this study, we evaluate the robustness of JATMO against HOUYI, a genetic attack framework that systematically mutates and optimizes adversarial prompts. We adapt HOUYI by introducing custom fitness scoring, modified mutation logic, and a new harness for local model testing, enabling a more accurate assessment of defense effectiveness. We fine-tuned LLaMA 2-7B, Qwen1.5-4B, and Qwen1.5-0.5B models under the JATMO methodology and compared them with a fine-tuned GPT-3.5-Turbo baseline. Results show that while JATMO reduces attack success rates relative to instruction-tuned models, it does not fully prevent injections; adversaries exploiting multilingual cues or code-related disruptors still bypass defenses. We also observe a trade-off between generation quality and injection vulnerability, suggesting that better task performance often correlates with increased susceptibility. Our results highlight both the promise and limitations of fine-tuning-based defenses and point toward the need for layered, adversarially informed mitigation strategies.

