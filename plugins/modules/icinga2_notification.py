from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = '''
    name: icinga2_notification
'''

def main():
    module = AnsibleModule(
        supports_check_mode=True,
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent']),
            name=dict(required=True),
            order=dict(default=10, type='int'),
            file=dict(required=True, type='str'),
            template=dict(default=False, type='bool'),
            apply=dict(default=False, type='bool'),
            apply_target=dict(type='str', choices=['Host', 'Service']),
            imports=dict(default=list(), type='list', elements='str'),
            host_name=dict(type='str'),
            service_name=dict(type='str'),
            _vars=dict(default=dict(), type='raw', aliases=['vars']),
            users=dict(type='list', elements='str'),
            user_groups=dict(type='list', elements='str'),
            times=dict(type='dict'),
            command=dict(type='str'),
            interval=dict(type='str'),
            period=dict(type='str'),
            zone=dict(type='str'),
            types=dict(type='list', elements='str'),
            states=dict(type='list', elements='str'),
            assign=dict(default=list(), type='list', elements='str'),
            ignore=dict(default=list(), type='list', elements='str'),
        )
    )

    args = module.params
    name = args.pop('name')
    order = args.pop('order')
    state = args.pop('state')
    file = args.pop('file')
    template = args.pop('template')
    imports = args.pop('imports')
    apply = args.pop('apply')
    apply_target = args.pop('apply_target')
    del args['_vars']

    module.exit_json(
        changed=False,
        args=args,
        name=name,
        order=str(order),
        state=state,
        file=file,
        template=template,
        imports=imports,
        apply=apply,
        apply_target=apply_target
    )


if __name__ == '__main__':
    main()
