---
layout: default
title: Beyond Context: Large Language Models Failure to Grasp Users Intent
---

# Beyond Context: Large Language Models Failure to Grasp Users Intent
**arXiv**：[2512.21110v1](https://arxiv.org/abs/2512.21110) · [PDF](https://arxiv.org/pdf/2512.21110.pdf)  
**作者**：Ahmed M. Hussain, Salahuddin Salahuddin, Panos Papadimitratos  

**一句话要点**：揭示大语言模型因缺乏上下文理解与意图识别能力导致安全漏洞

**关键词**：大语言模型安全, 意图识别, 上下文理解, 安全漏洞, 实证评估

## 3 点简述
- 核心问题：LLMs安全机制忽视上下文理解与用户意图识别，易被恶意利用。
- 方法要点：通过情感框架、渐进揭示和学术论证等技术实证评估多款先进LLMs。
- 实验或效果：推理配置加剧漏洞，Claude Opus 4.1在部分用例中优先意图检测。

## 摘要（原文）

> Current Large Language Models (LLMs) safety approaches focus on explicitly harmful content while overlooking a critical vulnerability: the inability to understand context and recognize user intent. This creates exploitable vulnerabilities that malicious users can systematically leverage to circumvent safety mechanisms. We empirically evaluate multiple state-of-the-art LLMs, including ChatGPT, Claude, Gemini, and DeepSeek. Our analysis demonstrates the circumvention of reliable safety mechanisms through emotional framing, progressive revelation, and academic justification techniques. Notably, reasoning-enabled configurations amplified rather than mitigated the effectiveness of exploitation, increasing factual precision while failing to interrogate the underlying intent. The exception was Claude Opus 4.1, which prioritized intent detection over information provision in some use cases. This pattern reveals that current architectural designs create systematic vulnerabilities. These limitations require paradigmatic shifts toward contextual understanding and intent recognition as core safety capabilities rather than post-hoc protective mechanisms.

