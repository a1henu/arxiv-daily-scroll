---
layout: default
title: Casting a SPELL: Sentence Pairing Exploration for LLM Limitation-breaking
---

# Casting a SPELL: Sentence Pairing Exploration for LLM Limitation-breaking
**arXiv**：[2512.21236v1](https://arxiv.org/abs/2512.21236) · [PDF](https://arxiv.org/pdf/2512.21236.pdf)  
**作者**：Yifan Huang, Xiaojun Jia, Wenbo Guo, Yuqiang Sun, Yihao Huang, Chong Wang, Yang Liu  

**一句话要点**：提出SPELL框架以评估大语言模型在恶意代码生成中的安全对齐弱点

**关键词**：大语言模型安全, 恶意代码生成, 越狱攻击, 安全对齐评估, AI辅助编码工具

## 3 点简述
- 核心问题：现有越狱研究较少针对恶意代码生成，存在安全对齐漏洞。
- 方法要点：采用时分选择策略，智能组合句子构建越狱提示，平衡探索与利用。
- 实验或效果：在三个先进代码模型上评估，攻击成功率最高达83.75%，真实工具中恶意代码生成率超73%。

## 摘要（原文）

> Large language models (LLMs) have revolutionized software development through AI-assisted coding tools, enabling developers with limited programming expertise to create sophisticated applications. However, this accessibility extends to malicious actors who may exploit these powerful tools to generate harmful software. Existing jailbreaking research primarily focuses on general attack scenarios against LLMs, with limited exploration of malicious code generation as a jailbreak target. To address this gap, we propose SPELL, a comprehensive testing framework specifically designed to evaluate the weakness of security alignment in malicious code generation. Our framework employs a time-division selection strategy that systematically constructs jailbreaking prompts by intelligently combining sentences from a prior knowledge dataset, balancing exploration of novel attack patterns with exploitation of successful techniques. Extensive evaluation across three advanced code models (GPT-4.1, Claude-3.5, and Qwen2.5-Coder) demonstrates SPELL's effectiveness, achieving attack success rates of 83.75%, 19.38%, and 68.12% respectively across eight malicious code categories. The generated prompts successfully produce malicious code in real-world AI development tools such as Cursor, with outputs confirmed as malicious by state-of-the-art detection systems at rates exceeding 73%. These findings reveal significant security gaps in current LLM implementations and provide valuable insights for improving AI safety alignment in code generation applications.

