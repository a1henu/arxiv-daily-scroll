---
layout: default
title: AI Gamestore: Scalable, Open-Ended Evaluation of Machine General Intelligence with Human Games
---

# AI Gamestore: Scalable, Open-Ended Evaluation of Machine General Intelligence with Human Games
**arXiv**：[2602.17594v1](https://arxiv.org/abs/2602.17594) · [PDF](https://arxiv.org/pdf/2602.17594.pdf)  
**作者**：Lance Ying, Ryan Truong, Prafull Sharma, Kaiya Ivy Zhao, Nathan Cloos, Kelsey R. Allen, Thomas L. Griffiths, Katherine M. Collins, José Hernández-Orallo, Phillip Isola, Samuel J. Gershman, Joshua B. Tenenbaum  

**一句话要点**：提出AI GameStore平台，通过人类游戏评估机器通用智能的开放性与可扩展性。

**关键词**：通用智能评估, 游戏基准测试, LLM合成, 人类循环, 视觉语言模型, 开放平台

## 3 点简述
- 核心问题：现有AI基准测试狭窄且易饱和，难以评估机器通用智能。
- 方法要点：利用LLMs和人类循环合成代表性人类游戏，构建游戏环境平台。
- 实验或效果：在100个游戏中评估VLMs，多数游戏得分低于人类平均10%，尤其在记忆和规划方面表现差。

## 摘要（原文）

> Rigorously evaluating machine intelligence against the broad spectrum of human general intelligence has become increasingly important and challenging in this era of rapid technological advance. Conventional AI benchmarks typically assess only narrow capabilities in a limited range of human activity. Most are also static, quickly saturating as developers explicitly or implicitly optimize for them. We propose that a more promising way to evaluate human-like general intelligence in AI systems is through a particularly strong form of general game playing: studying how and how well they play and learn to play \textbf{all conceivable human games}, in comparison to human players with the same level of experience, time, or other resources. We define a "human game" to be a game designed by humans for humans, and argue for the evaluative suitability of this space of all such games people can imagine and enjoy -- the "Multiverse of Human Games". Taking a first step towards this vision, we introduce the AI GameStore, a scalable and open-ended platform that uses LLMs with humans-in-the-loop to synthesize new representative human games, by automatically sourcing and adapting standardized and containerized variants of game environments from popular human digital gaming platforms. As a proof of concept, we generated 100 such games based on the top charts of Apple App Store and Steam, and evaluated seven frontier vision-language models (VLMs) on short episodes of play. The best models achieved less than 10\% of the human average score on the majority of the games, and especially struggled with games that challenge world-model learning, memory and planning. We conclude with a set of next steps for building out the AI GameStore as a practical way to measure and drive progress toward human-like general intelligence in machines.

