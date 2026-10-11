# Code Review Agent

## 1. 项目简介

Code Review Agent 是一个基于大语言模型的代码审查助手。

本项目可以读取本地代码文件，并通过大语言模型分析代码功能、潜在 Bug、异常情况以及改进建议。

## 2. 主要功能

- 读取本地代码文件
- 自动进行代码审查
- 查找潜在 Bug
- 分析异常和边界情况
- 提供代码优化建议
- 支持连续对话
- 支持上下文记忆
- 支持 API 调用失败自动重试
- 支持命令行交互

## 3. 技术栈

- Python 3.14
- OpenAI Python SDK
- 阿里云百炼 / 通义千问
- python-dotenv
- Visual Studio 2022

## 4. 项目结构

```text
CodeAgent/
│
├── CodeAgent.py
├── agent.py
├── tools.py
├── test.py
├── .env
├── README.md
└── Design.md